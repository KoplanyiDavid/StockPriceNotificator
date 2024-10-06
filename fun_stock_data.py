import requests
from constants import ALPHA_VANTAGE_API_URL

def get_stock_data() -> float:
    response = requests.get(ALPHA_VANTAGE_API_URL)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key,value) in data.items()]
    return(data_list[0]["4. close"])