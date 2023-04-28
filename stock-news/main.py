import requests
import os
import datetime as dt
from datetime import timedelta
import html
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


alpha_api_key = os.environ.get("ALPHA_API_KEY")


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

alpha_parameters = {
    "apikey": alpha_api_key,
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
}

alpha_response = requests.get("https://www.alphavantage.co/query", params=alpha_parameters)
alpha_data = alpha_response.json()

yesterday = (dt.datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
yesterday_open = float(alpha_data["Time Series (Daily)"][yesterday]["1. open"])
yesterday_close = float(alpha_data["Time Series (Daily)"][yesterday]["4. close"])


def check_change() -> bool:
    return abs(yesterday_close - (yesterday_open*1.05)) > 5


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

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
# print(get_news())

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


if check_change:
    for mail in get_news():
        msg_text = "Headline: "+mail["title"]+"\nBrief: "+mail["description"]
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+16205088752',
            to=os.environ.get("PHONE_NUMBER"),
            body=msg_text
        )
        print(message.status)


