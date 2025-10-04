import os, sqlite3, textwrap, json, datetime, time
from urllib.parse import urlparse
import requests, feedparser, yaml
from readability import Document
from markdownify import markdownify as md
from slugify import slugify
from openai import OpenAI
from pathlib import Path
import json, time, calendar, email.utils as eut
import random
import hashlib
from jinja2 import Environment, PackageLoader, select_autoescape
import re
    
env = Environment(
    loader=PackageLoader("blogroll"),
    autoescape=select_autoescape()
)

ROOT = Path(__file__).parent
STATE_PATH = ROOT / "data" / "state.json"
STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
if not STATE_PATH.exists(): STATE_PATH.write_text("{}", encoding="utf-8")
BLOGROLLS_DIR = ROOT / "blogrolls"
BLOGROLLS_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = "blogroll.db"
CFG_PATH = "feeds.yaml"

SYSTEM = """You are compiling a 'Daily Blogroll'—a terse, link-heavy roundup.
Style: one sentence per item (max ~30 words), credit the blog by name, add a quick take in a casual, conversational but concise manner.
Do not invent facts or quotes; stay within provided excerpts. You are given a suggested category per blog, but can override it if you feel another fits better, as the
author might have changed focus. Categories are: Gaming, Tech, Writing, General. Do not mention the source, title, url or category in the one-liner. You may
refer to the author by name if given.
Return JSON with an array 'items': [{source, title, url, one_liner, category}].
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
          "one_liner": {"type": "string", "maxLength": 200},
          "category": {"type": "string"}
        },
        "required": ["source", "url", "one_liner", "title", "category"],
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
    debug_log = []

    con = db()  # if you still use SQLite "seen" — keep it; helpful when timestamps are missing
    state = load_state()
    picked = []

    total_cap = cfg.get("max_items_total", 30)
    per_feed_cap = cfg.get("max_items_per_feed", 3)
    min_chars = cfg.get("min_chars_for_article", 500)
    skip_backlog = cfg.get("first_run_skip_backlog", True)

    # randomize the feed order a bit to avoid always picking the same ones first
    random.shuffle(cfg["feeds"])

    for f in cfg["feeds"]:
        debug_log.append(f"\nProcessing feed: {f.get('name','')} {f['url']}")
        if len(picked) >= total_cap:
            debug_log.append("Total cap reached, stopping.")
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
                debug_log.append("Feed cap reached, stopping.")
                break

            guid = getattr(e, "id", None) or getattr(e, "link", None)
            url = getattr(e, "link", "")
            if not guid or not url:
                debug_log.append(f"Skipping entry without GUID or URL: {e}")
                continue

            # Core filter: only newer than last_ts
            ts = entry_timestamp(e)
            if ts is not None and ts <= st.get("last_ts", 0):
                debug_log.append(f"Skipping entry older than last_ts: {e}")
                continue

            # (Optional) also keep your existing GUID-based de-dup:
            if already_seen(con, feed_url, guid):
                debug_log.append(f"Skipping already seen entry: {e}")
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
                    "category": f.get("category") or "General",
                    "published": published,
                    "title": title.strip(),
                    "excerpt": body[:3000],
                    "ts": ts or 0
                })
                pf_count += 1
                if ts: max_seen_ts = max(max_seen_ts, ts)
                time.sleep(0.3)
            except Exception:
                debug_log.append(f"Error processing entry: {e}")
                # ignore this entry on error
                pass

        # Update the cutoff for this feed to the max timestamp we actually used
        # If no items were processed but the feed changed, keep last_ts as-is.
        st["last_ts"] = max_seen_ts

        # persist after each feed to be crash-safe
        save_state(state)

    # write debug log
    with open(ROOT / "data" / "debug.log", "w", encoding="utf-8") as f:
        f.write("\n".join(debug_log) + "\n")
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
        CATEGORY: {it['category']}
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
                "text": f"Date: {today}. Create one-liners for these posts. Keep each line under ~30 words. Do not include the URL in the one-liner; it will be added automatically. If the author name is given, use that instead of the blog name when referring to the author of the blog within the one-liner. The category should be your best guess from Gaming, Tech, Writing, or General."},
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

    try:
        data = json.loads(resp.output[0].content[0].text)
    except Exception as e:
        print("Error parsing response:", e)
        # write to a file for inspection
        with open("debug_response.json", "w", encoding="utf-8") as f:
            f.write(resp.output[0].content[0].text)
        return []

    return data["items"]

def find_previous_blogroll():
    # find the latest blogroll before today
    files = list(BLOGROLLS_DIR.glob("daily-blogroll-*.html"))
    files = [f for f in files if f.stem != "latest"]
    files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    return files[0].name if files else None

def render_html(blog_title, items):
    """Simple HTML rendering (not used by default) render
    renders to a grid 3 across and up to 4 down, each element has the CSS class 'feed-element'
    should be contained in a <div class="feed-grid">...</div>
    title in heading, each cell should be a div with a the blog name/link in bold, then the one-liner
    """
    jinja_vars = {}
    title = f"{blog_title}: {datetime.date.today().isoformat()}"
    jinja_vars["title"] = title

    previous_blog = find_previous_blogroll()
    if previous_blog:
        jinja_vars["previous"] = previous_blog

    # sort item list by category, then source
    items.sort(key=lambda x: (x.get("category",""), x["source"].lower()))

    jinja_item_list = []
    alt_text_list = []

    for it in items:
        item_dict = {}
        item_dict["source"] = it["source"]
        item_dict["url"] = it["url"]
        item_dict["one_liner"] = it["one_liner"].rstrip()
        alt_text_list.append(item_dict["one_liner"])
        source_image_ref = 'images/' + string_to_hash(it["source"]) + '.png'
        if os.path.exists(BLOGROLLS_DIR / source_image_ref):
            item_dict["image"] = source_image_ref
        jinja_item_list.append(item_dict)

    jinja_vars["blogs"] = jinja_item_list
    template = env.get_template("dailyblogtemplate.html")
    output = template.render(vars=jinja_vars)

    slug = slugify(title)
    filename = f"{slug}.html"
    path = BLOGROLLS_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        f.write(output)
    with open(BLOGROLLS_DIR / "index.html", "w", encoding="utf-8") as f:
        template = env.get_template("latesttemplate.html")
        f.write(template.render(today=filename))
    with open(BLOGROLLS_DIR / "latest.txt", "w", encoding="utf-8") as f:
        f.write("\n\n".join(alt_text_list) + "\n")
    return path, title

def render_markdown(blog_title, items):
    # Optionally group by source for a “multiple links per blog” look
    title = f"{blog_title}: {datetime.date.today().isoformat()}"
    lines = [f"# {title}", ""]

    # make a map of items with key being category and value being a list of items with that category
    category_map = {}
    for it in items:
        category = it.get("category", "Uncategorized")
        if category not in category_map:
            category_map[category] = []
        category_map[category].append(it)

    # output items by category with a heading for each category
    for category, cat_items in category_map.items():
        lines.append(f"## {category}\n")
        for it in cat_items:
            # bullet: blog name — one-liner (with link)
            lines.append(f"- **[{it['source']}]({it['url']})** — {it['one_liner'].rstrip()}")
            
    md = "\n".join(lines) + "\n"
    path = BLOGROLLS_DIR / "latest.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    return path, title

def main():
    cfg = load_cfg()
    items = collect_new_items(cfg)
    if not items:
        print("No fresh posts.")
        return
    # Keep the order stable but not biased: sort by source, then title
    items = items[:cfg.get("max_items_total", 30)]
    drafted = call_model(items)
    md_path, _ = render_markdown(cfg.get("title","Daily Blogroll"), drafted)

    print("Wrote", md_path)
    md_path, _ = render_html(cfg.get("title","Daily Blogroll"), drafted)
    print("Wrote", md_path)
    renavigate_blogrolls()

def get_sorted_blogrolls():
    """
    Find all daily blogroll HTML files and return them sorted by date (oldest first).
    
    Returns:
        List of tuples where each tuple contains (date_string, full_filename)
    """
    # Get all HTML files in the blogrolls directory
    files = list(BLOGROLLS_DIR.glob("daily-blogroll-*.html"))
    
    # Pattern to extract date components
    pattern = r"daily-blogroll-(\d{4})-(\d\d)-(\d\d)\.html"
    
    # Create list of tuples (date_string, full_filename)
    result = []
    for file_path in files:
        filename = file_path.name
        match = re.match(pattern, filename)
        if match:
            year, month, day = match.groups()
            date_string = f"{year}{month}{day}"
            result.append((date_string, filename))
    
    # Sort by date string (which will be in YYYYMMDD format)
    result.sort(key=lambda x: x[0])
    
    return result

def renavigate_blogrolls():
    """
    Go through all blogroll HTML files and add navigation links to previous and next blogrolls.
    """
    blogrolls = get_sorted_blogrolls()
    for i, (datestr, filename) in enumerate(blogrolls):
        with open(BLOGROLLS_DIR / filename, "r+", encoding="utf-8") as f:
            content = f.read()
            # separate the content before the <h1> tag into a variable "prelude" and the content after the </h1> tag as the antelude
            prelude, starttag, _ = content.partition("<h1>")
            _, endtag, antelude = content.partition("</h1>")
            header = ''
            # Add navigation links
            if i > 0:
                _, prev_filename = blogrolls[i - 1]
                header = header + f'<a href="{prev_filename}">⬅️</a>'
            header = header + f'<a href="latest.html">Daily Blogroll: {datestr[0:4]}-{datestr[4:6]}-{datestr[6:8]}</a>'
            if i < len(blogrolls) - 1:
                _, next_filename = blogrolls[i + 1]
                header = header + f'<a href="{next_filename}">➡️</a>'
            new_h1 = f"<h1>{header}</h1>"
            content = prelude + new_h1 + antelude
            f.seek(0)
            f.write(content)
            f.truncate()
    print("Renavigated blogrolls.")

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

def string_to_hash(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    main()
