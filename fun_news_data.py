import requests
from constants import NEWS_API_URL

def get_news_data(news_num: int) -> list:
    response = requests.get(NEWS_API_URL)
    response.raise_for_status()
    articles = response.json()["articles"]

    three_articles = articles[:news_num]
    formatted_articles = [f"Headline: {article["title"]}\nBrief: {article["description"]}" for article in three_articles]

    return formatted_articles