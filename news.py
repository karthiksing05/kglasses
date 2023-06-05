from gnewsclient import gnewsclient

from pyshorteners import Shortener

def shorten_link(url):
    url_shortener = Shortener() 
    return url_shortener.tinyurl.short(url)

def get_news():
    news_headlines = []
    topics = [
        "World",
        "Nation",
        "Business",
        "Technology",
        "Entertainment",
        "Sports"
    ]
    for topic in topics:
        client = gnewsclient.NewsClient(
            language="english", 
            location="United States", 
            topic=topic, 
            max_results=1
        )
        news_headlines.append([f"{x['title']}: {shorten_link(x['link'])}" for x in client.get_news()])
    return news_headlines

if __name__ == "__main__":
    print(get_news())