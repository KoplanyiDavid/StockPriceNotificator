from datetime import datetime
import time
from fun_news_data import get_news_data
from fun_stock_data import get_stock_data
from fun_messaging import send_message

# Check stock price movement within 2 days
last_day_price = get_stock_data(number_of_days_before=0)
day_before_last_day_price = get_stock_data(number_of_days_before=1)
difference_in_percentage = (abs(1 - (last_day_price / day_before_last_day_price))) * 100

message = ""

# send the message at 8am in the morning if the movement is bigger than 5%
if 8 == datetime.now().hour and difference_in_percentage > 5:

    # construct the message
    message += f"SEDG closing price: {last_day_price}"
    for news in get_news_data(news_num=2):
        message += "\n"
        message += str(news)

    # if the message send was not successful wait 60 seconds and try again
    while not send_message(message):
        time.sleep(60)