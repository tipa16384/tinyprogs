import os, sqlite3, textwrap, json, datetime, time
from urllib.parse import urlparse
import requests, feedparser, yaml
from readability import Document
from markdownify import markdownify as md
from slugify import slugify
from openai import OpenAI
from pathlib import Path
import json, time, calendar, email.utils as eut

ROOT = Path(__file__).parent
STATE_PATH = ROOT / "data" / "state.json"
STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
if not STATE_PATH.exists(): STATE_PATH.write_text("{}", encoding="utf-8")

DB_PATH = "blogroll.db"
CFG_PATH = "feeds.yaml"

SYSTEM = """You are compiling a 'Daily Blogroll'—a terse, link-heavy roundup.
Style: one sentence per item (max ~30 words), credit the blog by name, add a quick take in a casual, conversational but concise manner.
Do not invent facts or quotes; stay within provided excerpts.
Return JSON with an array 'items': [{source, title, url, one_liner}].
"""

SCHEMA = {
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source": {"type": "string"},
          "title":  {"type": "string"},
          "url":    {"type": "string"},
          "one_liner": {"type": "string", "maxLength": 200}
        },
        "required": ["source", "url", "one_liner", "title"],
        "additionalProperties": False
      }
    }
  },
  "required": ["items"],
  "additionalProperties": False
}

def db():
    con = sqlite3.connect(DB_PATH)
    con.execute("""CREATE TABLE IF NOT EXISTS seen(
        feed TEXT, guid TEXT, url TEXT, published TEXT, seen_at TEXT,
        PRIMARY KEY(feed, guid)
    )""")
    return con

def mark_seen(con, feed, guid, url, published):
    con.execute("INSERT OR IGNORE INTO seen(feed,guid,url,published,seen_at) VALUES(?,?,?,?,datetime('now'))",
                (feed, guid, url, published))
    con.commit()

def already_seen(con, feed, guid):
    return con.execute("SELECT 1 FROM seen WHERE feed=? AND guid=?", (feed, guid)).fetchone() is not None

def fetch_readable(url, timeout=15):
    r = requests.get(url, timeout=timeout, headers={"User-Agent":"DailyBlogrollBot/1.0"})
    r.raise_for_status()
    doc = Document(r.text)
    html = doc.summary()
    text = md(html)
    title = (doc.title() or "").strip()
    # fallback if readability failed
    if len(text.strip()) < 200:
        text = md(r.text)
    return title, text

def load_cfg():
    with open(CFG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def collect_new_items(cfg):
    con = db()  # if you still use SQLite "seen" — keep it; helpful when timestamps are missing
    state = load_state()
    picked = []

    total_cap = cfg.get("max_items_total", 30)
    per_feed_cap = cfg.get("max_items_per_feed", 3)
    min_chars = cfg.get("min_chars_for_article", 500)
    skip_backlog = cfg.get("first_run_skip_backlog", True)

    for f in cfg["feeds"]:
        if len(picked) >= total_cap:
            break

        feed_url = f["url"]
        st = state.setdefault(feed_url, {})
        # On very first run for this feed, set the cutoff to "now" to avoid mining history
        if "last_ts" not in st and skip_backlog:
            st["last_ts"] = int(time.time())

        # Use HTTP conditionals if we have them
        parsed = feedparser.parse(
            feed_url,
            etag=st.get("etag"),
            modified=st.get("modified")
        )

        # Save fresh etag/modified returned by server
        if getattr(parsed, "etag", None):
            st["etag"] = parsed.etag
        if getattr(parsed, "modified", None):
            # parsed.modified is time.struct_time (UTC)
            st["modified"] = parsed.modified

        pf_count = 0
        max_seen_ts = st.get("last_ts", 0)

        for e in parsed.entries:
            if len(picked) >= total_cap or pf_count >= per_feed_cap:
                break

            guid = getattr(e, "id", None) or getattr(e, "link", None)
            url = getattr(e, "link", "")
            if not guid or not url:
                continue

            # Core filter: only newer than last_ts
            ts = entry_timestamp(e)
            if ts is not None and ts <= st.get("last_ts", 0):
                continue

            # (Optional) also keep your existing GUID-based de-dup:
            if already_seen(con, feed_url, guid):
                continue

            title = getattr(e, "title", "") or "(untitled)"
            published = getattr(e, "published", "") or getattr(e, "updated", "")

            # Mark seen early so a later crash won't re-queue it
            mark_seen(con, feed_url, guid, url, published)

            # Fetch readable content
            try:
                atitle, body = fetch_readable(url)
                if atitle and not title:
                    title = atitle
                if len(body) < min_chars:
                    continue
                picked.append({
                    "source": f.get("name") or urlparse(feed_url).netloc,
                    "author": f.get("blogger") or "",
                    "feed_url": feed_url,
                    "url": url,
                    "published": published,
                    "title": title.strip(),
                    "excerpt": body[:3000],
                    "ts": ts or 0
                })
                pf_count += 1
                if ts: max_seen_ts = max(max_seen_ts, ts)
                time.sleep(0.3)
            except Exception:
                # ignore this entry on error
                pass

        # Update the cutoff for this feed to the max timestamp we actually used
        # If no items were processed but the feed changed, keep last_ts as-is.
        st["last_ts"] = max_seen_ts

        # persist after each feed to be crash-safe
        save_state(state)

    return picked

def call_model(items):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    #print (f"Client: {dir(client)}")

    today = datetime.date.today().strftime("%B %d, %Y")

    # Build compact user content
    chunks = []
    for it in items:
        chunks.append(textwrap.dedent(f"""
        SOURCE: {it['source']}
        TITLE: {it['title']}
        URL: {it['url']}
        PUBLISHED: {it['published']}
        AUTHOR: {it['author']}
        EXCERPT:
        {it['excerpt']}
        """).strip())

    resp = client.responses.create(
        model="gpt-4o",
        instructions=SYSTEM,
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text",
                "text": f"Date: {today}. Create one-liners for these posts. Keep each line under ~30 words. Do not include the URL in the one-liner; it will be added automatically. If the author name is given, use that instead of the blog name when referring to the author of the blog within the one-liner."},
                *[{"type": "input_text", "text": c} for c in chunks],
            ],
        }],
        text={
            "format": {
                "type": "json_schema",
                "name": "DailyBlogrollItems",  # <-- required here
                "schema": SCHEMA,              # <-- your Python dict schema
                "strict": True                 # optional but recommended
            }
        },
#        temperature=0.3,
        max_output_tokens=1500,
        metadata={"prompt_cache_key": "daily-blogroll-v1"},
    )

    data = json.loads(resp.output[0].content[0].text)
    return data["items"]

def render_markdown(blog_title, items):
    # Optionally group by source for a “multiple links per blog” look
    title = f"{blog_title}: {datetime.date.today().isoformat()}"
    lines = [f"# {title}", ""]
    for it in items:
        # bullet: blog name — one-liner (with link)
        lines.append(f"- **[{it['source']}]({it['url']})** — {it['one_liner'].rstrip()}")
    md = "\n".join(lines) + "\n"
    slug = slugify(title)
    path = f"{slug}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    return path, title

# --- (Optional) auto-post to WordPress ---
def post_to_wordpress(md_path, wp_url, username, app_password, status="draft"):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    # very basic: first line is H1 title, strip it from content
    first_nl = content.find("\n")
    title = content[2:first_nl].strip() if content.startswith("# ") else "Daily Blogroll"
    body = content[first_nl:].strip() if first_nl > 0 else content

    api = wp_url.rstrip("/") + "/wp-json/wp/v2/posts"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "User-Agent": "DailyBlogrollBot/1.0 (+https://chasingdings.com)"
    }
    payload = {"title": title, "content": body, "status": status}
    r = requests.post(api,
        auth=(username, app_password),
        headers=headers,
        data=json.dumps(payload))
    r.raise_for_status()
    return r.json().get("link")

def main():
    cfg = load_cfg()
    items = collect_new_items(cfg)
    if not items:
        print("No fresh posts.")
        return
    # Keep the order stable but not biased: sort by source, then title
    items = items[:cfg.get("max_items_total", 30)]
    drafted = call_model(items)
    md_path, title = render_markdown(cfg.get("title","Daily Blogroll"), drafted)

    print("Wrote", md_path)
    # Auto-post if env vars are present
    wp_url = os.getenv("WP_URL")
    if None and wp_url:
        link = post_to_wordpress(
            md_path,
            wp_url=wp_url,
            username=os.getenv("WP_USER"),
            app_password=os.getenv("WP_APP_PASSWORD"),
            status=os.getenv("WP_STATUS","draft")
        )
        print("WordPress:", link)

def load_state():
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))

def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")

def entry_timestamp(entry) -> int | None:
    # Prefer structured times (UTC struct_time)
    for key in ("published_parsed", "updated_parsed", "created_parsed"):
        t = getattr(entry, key, None)
        if t: 
            return calendar.timegm(t)  # struct_time is UTC

    # Fallback: parse RFC2822/ISO-ish strings if present
    for key in ("published", "updated"):
        s = getattr(entry, key, None)
        if s:
            try:
                dt = eut.parsedate_to_datetime(s)
                # If tz-naive, treat as UTC
                if dt.tzinfo is None:
                    return int(dt.replace(tzinfo=datetime.timezone.utc).timestamp())
                return int(dt.timestamp())
            except Exception:
                pass
    return None

if __name__ == "__main__":
    main()
