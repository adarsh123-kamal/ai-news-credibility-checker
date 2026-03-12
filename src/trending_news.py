import feedparser

def get_trending_news():

    url = "https://news.google.com/rss"

    feed = feedparser.parse(url)

    news = []

    for entry in feed.entries[:10]:

        news.append({
            "title": entry.title,
            "link": entry.link
        })

    return news