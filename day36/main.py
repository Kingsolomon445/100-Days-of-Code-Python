import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client

NEWS_API_KEY = ""
STOCK_API_KEY = ""
TWILIO_ACCT_SID = ""
TWILIO_AUTH_TOKEN = ""
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY,
}


def calculate_percentage(before_previous_day_price, diff_price):
    percent = diff_price / before_previous_day_price * 100
    return round(percent)


response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
yesterday = date.today() - timedelta(days=1)
day_before_yesterday = yesterday - timedelta(days=1)
yesterday_close = float(stock_data["Time Series (60min)"][f"{yesterday} 20:00:00"]["4. close"])
day_before_yesterday_close = float(stock_data["Time Series (60min)"][f"{day_before_yesterday} 20:00:00"]["4. close"])
diff = yesterday_close - day_before_yesterday_close
diff = abs(diff)
percentage = calculate_percentage(day_before_yesterday_close, diff)

if percentage > 5:
    news_parameters = {
        "q": STOCK,
        "qInTitle": COMPANY_NAME,
        "from": "2022-11-24",
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    articles = news_data["articles"]
    articles = articles[:3]


news_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in articles]

client = Client(TWILIO_ACCT_SID, TWILIO_AUTH_TOKEN)

for article in news_articles:
    message = (client.messages.create(
        body=article,
        from_="+",
        to="+",
    ))
