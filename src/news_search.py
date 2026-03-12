import feedparser
import urllib.parse

def search_news(query):

    # convert spaces to URL-safe format
    encoded_query = urllib.parse.quote_plus(query)

    # correct full Google News RSS URL
    url = f"https://news.google.com/rss/search?q={encoded_query}"

    feed = feedparser.parse(url)

    results = []

    for entry in feed.entries[:5]:
        results.append({
            "title": entry.title,
            "link": entry.link
        })

    return results