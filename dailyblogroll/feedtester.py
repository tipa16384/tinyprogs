import feedparser
import yaml

feed_list = [
'http://scripting.com/rss.xml'
]

feed_yaml = 'feeds.yaml'

def test_feed(feed):
    """
    Reads an RSS feed and checks for expected content.
    """
    parsed_feed = feedparser.parse(feed)
    #assert parsed_feed.bozo == 0, "Failed to parse feed"
    assert 'entries' in parsed_feed, "No entries found in feed"
    print (parsed_feed.entries)
    assert len(parsed_feed.entries) > 0, "Empty feed"
    # Check for specific content in the feed
    for entry in parsed_feed.entries:
        assert 'link' in entry, "Missing link in entry"
        assert 'published' in entry, "Missing published date in entry"
        print (f"Link: {entry.link}, Published: {entry.published}")

if __name__ == "__main__":
    # read YAML file for additional feeds
    # with open(feed_yaml, 'r', encoding='utf-8') as f:
    #     feeds_from_yaml = yaml.safe_load(f)
    #     for feed in feeds_from_yaml.get('feeds', []):
    #         feed_list.append(feed['url'])
    for feed_url in feed_list:
        try:
            test_feed(feed_url)
            print(f"Feed test for {feed_url} passed successfully.")
        except AssertionError as e:
            print(f"Feed test for {feed_url} failed: {e}")
