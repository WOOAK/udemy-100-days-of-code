# Second approach: Using last refresh date provided in json-completed
import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "SVPHFK3O9HKBYMM7"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "outputsize":"compact",
    "apikey":API_KEY
}
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)

data = response.json()
# today = (dt.datetime.now()).date()
# because using last refresh date, no need looping
def get_prev_day(last_date):
    day_gap = 1

    # get weekday
    weekday = last_date.strftime("%w")
    # close market on weekend, weekday = 0 is sunday
    if weekday == "1":
        day_gap = 3
    elif weekday == "0":
        day_gap = 2

    # print(day_gap)
    diff_day = dt.timedelta(days=day_gap)

    prev_day = last_date - diff_day
    return prev_day


def get_news():
    API_KEY = "46db0d9c2c86412b9546cbd8c72986ab"
    parameters = {
        "q": "苹果电脑",
        "sortBy": "publishedAT",
        "apiKey":API_KEY
    }
    response = requests.get(url="http://newsapi.org/v2/everything",params=parameters)
    news_data = response.json()

    return news_data["articles"]

def send_news(news, is_decrease, percent):
    if is_decrease:
        symbol = "🔻"
    else:
        symbol = "🔺"
    account_sid = "AC77b240fca3f56d154ed8678144255a93"
    auth_token = "324e8049e647639df2ceb745684ab07d"

    client = Client(account_sid, auth_token)

    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+601137837026'
    for count in range(3):
        title = news[count]["title"]
        content = news[count]["content"]
        link = news[count]["url"]
        body = f"{STOCK}: {symbol}{percent}%\nHeading: {title}\nBrief: {content}\nLink: {link}"
        client.messages.create(body= body,
                               from_=from_whatsapp_number,
                               to=to_whatsapp_number)

def calculate_percentage(Day_minus_1, Day_minus_2):
    is_decrease = False
    Day_minus_1_close = float(data["Time Series (Daily)"][str(Day_minus_1)]["4. close"])
    Day_minus_2_close = float(data["Time Series (Daily)"][str(Day_minus_2)]["4. close"])
    diff = Day_minus_1_close - Day_minus_2_close
    percent = diff/Day_minus_1_close * 100
    if percent < 0:
        is_decrease = True
    print(percent)
    percent = round(abs(percent),2)
    if percent >= 3:
        news_content = get_news()
        send_news(news_content, is_decrease, percent)

# get last refresh date and convert from string to datetime format
last_date_str = data["Meta Data"]["3. Last Refreshed"]
last_date_obj = (dt.datetime.strptime(last_date_str, '%Y-%m-%d')).date()
previous_day = get_prev_day(last_date_obj)
# last refresh date as first parameter, second parameter is the market open day before last refresh date
calculate_percentage(last_date_obj,previous_day)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


