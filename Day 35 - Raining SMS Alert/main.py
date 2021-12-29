import requests
import datetime as dt
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os
from dotenv import load_dotenv

# twilio account sign up
account_sid = "AC77b240fca3f56d154ed8678144255a93"
# auth_token = "324e8049e647639df2ceb745684ab07d"
lon = 101.6865
lat = 3.
# Environment variable -> cater complexity and security for some private keys
# first approach
# environment variable, store the value in Terminal. type 'env', type "export variable = value", then get back the
# value using environ.get("variable")-not work, can load after manually add in edit configuration
# https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm
# second approach
# try load_dotenv
# load_dotenv("/Users/aykuanwoo/PycharmProjects/day-35/sec.txt")
api_key = os.getenv("API_KEY")
auth_token = os.getenv("AUTH_TOKEN")
# api_key = os.environ["API_KEY"]
# auth_token = os.environ["AUTH_TOKEN"]
print(api_key)
print(auth_token)
# openweather website API, some api website need API key to grant authority
location = {
    "lon": 101.6865,
    "lat": 3.1431,
    "appid": api_key,
#    "appid": "ffa39c9988facd977b05e7f20ad135e2",
    "exclude":"current,minutely,daily"
}
today = dt.datetime.now()
hour = today.hour
print(hour)
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params= location)
response.raise_for_status()
data = response.json()
pm_or_am = "am"
for hours in range(12):
    weather_id = data["hourly"][hours]["weather"][0]["id"]
# print(data)
    print(weather_id)
    if weather_id < 700:
        rain_time = hour + hours
        # this logic applies only if start time is before 12pm, haven't fix 12pm/12am bug yet
        if rain_time > 11:
            pm_or_am = "pm"
            rain_time -= 12
        proxy_client = TwilioHttpClient()
        # for python anywhere
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

        print(f"Bring umbrella, it may rain at {rain_time}{pm_or_am}")
        client = Client(account_sid,auth_token, http_client=proxy_client)
        message = client.messages \
            .create(
            body=f"Bring umbrella☔️, it may rain at {rain_time}{pm_or_am}",
            from_='+18054214482',
            to='+60122486339'
        )
        print(message.status)
        break

# next12 = data["hourly"][:12]
# if any(i["weather"][0]["id"] < 700 for i in next12):
#     print("rain")
#
# a nice function that checks if there's at least one True in your check

# weather_code_list = [hour["weather"][0]["id"] for hour in weather_data["hourly"][:11] if hour["weather"][0]["id"] < 700]

# if weather_code_list != []:
#     print("bring an umbrella")

