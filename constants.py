from decouple import config

ALPHA_VANTAGE_API_KEY = config("ALPHA_VANTAGE_API_KEY", cast=str)
STOCK_SYMBOL = "SEDG"
ALPHA_VANTAGE_API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_SYMBOL}&outputsize=compact&apikey={ALPHA_VANTAGE_API_KEY}"

NEWS_API_KEY = config("NEWS_API_KEY", cast=str)
NEWS_API_URL = f"https://newsapi.org/v2/everything?q=SEDG&apiKey={NEWS_API_KEY}"

CHAT_ID = config("CHAT_ID")
BOT_TOKEN = config("BOT_TOKEN")