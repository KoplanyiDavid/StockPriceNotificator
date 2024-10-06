import requests
from constants import NEWS_API_URL

def get_news_data() -> list:
    response = requests.get(NEWS_API_URL)
    response.raise_for_status()
    data = response.json()

    news_list = []
    for news in data["articles"]:
        news_list.append(news["content"])

    return news_list