import requests
from twilio.rest import Client
import os
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "02WA3LJLGQNKV6ET"
NEWS_API_KEY = "52255cf86a7540208271a0ca2aa87f5a"
TWILIO_ACCOUNT_SID = "ACf05e4ecd2e28e38f0a6602cea4931e19"

TWILIO_AUTH_TOKEN = "8d8f3a11ce17b9a566720d0ff17e9929"


def send_message(delta_percent, stock, data):

    for item in data:
        account_sid = TWILIO_ACCOUNT_SID
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        # auth_token = TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        body_str = f"{stock}: {'🔺' if delta_percent > 0 else '🔻'}{abs(delta_percent)}%\nHeadline: {item[0]}.\nBrief: {item[1]}"
        message = client.messages \
            .create(
                body=body_str,
                from_='+16266997586',
                to='+84397479959'
            )


def get_news(delta_percent, company, stock):
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": company,
        "sortBy": "popularity"
    }
    data = requests.get(url, params=params).json()
    my_data = [(x["title"], x["description"]) for x in data["articles"][:3]]
    send_message(delta_percent, stock, my_data)


def main():

    # STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": API_KEY
    }
    url = 'https://www.alphavantage.co/query'
    r = requests.get(url, params=params)
    data = r.json()
    price_data = data["Time Series (Daily)"].items()
    close_price_list = [y["4. close"] for (x, y) in price_data]

    y_close_price = float(close_price_list[0])
    dby_close_price = float(close_price_list[1])
    delta_percent = round((y_close_price/dby_close_price)*100) - 100
    if delta_percent >= 1 or delta_percent <= -5:
        get_news(delta_percent, COMPANY_NAME, STOCK)

    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    # Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """


if __name__ == '__main__':
    main()
