import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "NIQPIK8C9B7Q7T5U"
ALPHA_API_URL = "https://www.alphavantage.co/query"
parameters = {
    "function": 'TIME_SERIES_DAILY_ADJUSTED',
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

response = requests.get(ALPHA_API_URL, params=parameters)
response.raise_for_status()
stocks_data = response.json()

stock_slice = stocks_data['Time Series (Daily)']
stocks_data_list = [value for (key, value) in stock_slice.items()]
last_day = float(stocks_data_list[0]['4. close'])
day_before = float(stocks_data_list[1]['4. close'])
the_day_before = float(stocks_data_list[2]['4. close'])

difference = abs(day_before - the_day_before)

diff_percent = (difference / last_day) * 100

if diff_percent > 5:
    print("get news")
    # response = requests.get(news site, params=parameters)
    # response.raise_for_status()
    # news = response.json()


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

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

