# First approach: Without using last refresh date provided in json, but using current day by now()-incomplete
import requests
import datetime as dt
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
today = (dt.datetime.now()).date()

# different with second approach, this function need to loop, until it get a key (happens on close market in midnight)
def get_prev_day(current_day):
    day_gap = 1

    weekday = current_day.strftime("%w")
    # print(weekday)
    if weekday == "1":
        day_gap = 3
    elif weekday == "0":
        day_gap = 2

    # print(day_gap)
    diff_day = dt.timedelta(days=day_gap)

    prev_day = current_day - diff_day
    print(str(prev_day))

    while str(prev_day) not in data["Time Series (Daily)"]:
        saved_date = prev_day
        prev_day = get_prev_day(saved_date)
    return prev_day

def get_news():
    API_KEY = "46db0d9c2c86412b9546cbd8c72986ab"
    parameters = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAT",
        "apiKey":API_KEY
    }
    response = requests.get(url="http://newsapi.org/v2/everything",params=parameters)
    news_data = response.json()
    print(news_data)

def calculate_percentage(Day_minus_1, Day_minus_2):

    Day_minus_1_close = float(data["Time Series (Daily)"][str(Day_minus_1)]["4. close"])
    Day_minus_2_close = float(data["Time Series (Daily)"][str(Day_minus_2)]["4. close"])
    diff = Day_minus_1_close - Day_minus_2_close
    percent = abs((diff/Day_minus_1_close) * 100)
    print(percent)
    if percent >= 3:
        get_news()


previous_day = get_prev_day(today)
previous_of_previous_day = get_prev_day(previous_day)
calculate_percentage(previous_day, previous_of_previous_day)


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


