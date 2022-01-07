from gnewsclient import gnewsclient
import PySimpleGUI as sg

import requests

def shorten_link(url):
    api_key = "7d087ea641ba07276fdb5037b58f5717d6172"
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    data = requests.get(api_url).json()["url"]
    if data["status"] == 7:
        shortened_url = data["shortLink"]
        return shortened_url
    else:
        print("[!] Error Shortening URL:", data)

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
