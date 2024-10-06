from datetime import datetime
import time
from fun_news_data import get_news_data
from fun_stock_data import get_stock_data
from fun_messaging import send_message


message = ""

# send the message at 8am in the morning
if True: #8 == datetime.now().hour:

    # construct the message
    message += f"SEDG closing price: {get_stock_data()}"
    for news in get_news_data():
        message += "\n"
        message += str(news)

    # if the message send was not successful wait 60 seconds and try again
    while not send_message(message):
        time.sleep(60)