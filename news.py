from gnewsclient import gnewsclient
import PySimpleGUI as sg

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
        news_headlines.append([str(x["title"]) for x in client.get_news()])
    return news_headlines
