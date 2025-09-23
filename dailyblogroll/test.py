import os, requests, json

WP = "https://chasingdings.com/wp-json/wp/v2/posts"
AUTH = (os.getenv("WP_USER"), os.getenv("WP_APP_PASSWORD"))
print (AUTH)
HEADERS = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json",
    "User-Agent": "DailyBlogrollBot/1.0 (+https://chasingdings.com)"
}
payload = {"title": "API test", "status": "draft", "content": "Hello from the API."}

r = requests.post(WP, auth=AUTH, headers=HEADERS, data=json.dumps(payload))
print(r.status_code, r.text)
r.raise_for_status()
