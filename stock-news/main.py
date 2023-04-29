import requests
import os
import datetime as dt
from datetime import timedelta
import html
from twilio.rest import Client

STOCK = "TSLA"
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
alpha_api_key = os.environ.get("ALPHA_API_KEY")

alpha_parameters = {
    "apikey": alpha_api_key,
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
}
alpha_response = requests.get("https://www.alphavantage.co/query", params=alpha_parameters)
alpha_data = alpha_response.json()

yesterday = (dt.datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
before_day_yesterday = (dt.datetime.today() - timedelta(days=2)).strftime("%Y-%m-%d")

before_day_yesterday_close = float(alpha_data["Time Series (Daily)"][before_day_yesterday]["4. close"])
yesterday_close = float(alpha_data["Time Series (Daily)"][yesterday]["4. close"])


def check_change(yesterday_close_price, before_day_close_price):
    diff = yesterday_close_price - before_day_close_price
    return (diff / yesterday_close)*100


def get_news():
    top_news = []
    news_parameters = {
        "apiKey": "45559f545b484d20a7d8a6eb0097dede",
        "q": STOCK,
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()

    for i in range(3):
        top_news.append(
            {
                "title": html.unescape(news_data["articles"][i]["title"]),
                "description": html.unescape(news_data["articles"][i]["description"])
            }
        )
    return top_news


change_percent = check_change(yesterday_close, before_day_yesterday_close)
if abs(change_percent) > 5:
    change_direction = "Up" if change_percent > 0 else "Down"
    for mail in get_news():
        msg_text = f"{STOCK}: {change_direction} %{int(change_percent)} " \
                   f"\nHeadline: {mail['title']}\nBrief: {mail['description']}"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+16205088752',
            to=os.environ.get("PHONE_NUMBER"),
            body=msg_text
        )
        print(message.status)
