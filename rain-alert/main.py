import os
import requests
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = os.environ.get("API_KEY")

weather_params = {
    "lat" : 40.758400,
    "lon" : 33.760510,
    "exclude" : "current,minutely,daily",
    "appid" : api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

def bring_umbrella():
    for i in range(12):
        if weather_data["hourly"][i]["weather"][0]["id"] < 700:
            return True
    return False

if bring_umbrella():
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        from_='+16205088752',
        to='+905399134126',
        body="It's going to rain today. Remember to bring an umbrella!"
    )
    print(message.status)


