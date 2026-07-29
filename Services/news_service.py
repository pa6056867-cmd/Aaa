import feedparser


RSS_URL = "https://www.zoomit.ir/feed/"


def get_news():

    feed = feedparser.parse(RSS_URL)

    news = []

    for item in feed.entries[:5]:

        news.append(
            {
                "title": item.title,
                "link": item.link
            }
        )

    return news
