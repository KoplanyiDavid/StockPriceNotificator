import requests
from constants import ALPHA_VANTAGE_API_URL

def get_stock_data(number_of_days_before: int) -> float:

    if number_of_days_before < 0 or number_of_days_before > 20:
        print("Number of days before must be between 0 and 20!")
        raise ValueError
    
    response = requests.get(ALPHA_VANTAGE_API_URL)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key,value) in data.items()]
    return(data_list[number_of_days_before]["4. close"])