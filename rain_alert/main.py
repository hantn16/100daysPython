from twilio.rest import Client
import os
import requests
MY_LAT = 20.941660
MY_LONG = 107.123650
MY_OWM_APIKEY = "b6bc30a694baf40944ba59974692dbf6"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_OWM_APIKEY,
    "exclude": "current,daily,minutely,alerts"
}
res = requests.get(OWM_ENDPOINT, weather_params)
res.raise_for_status()
weather_data = res.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_12hours_next_data = weather_data["hourly"][:12]
lst_weather_code = [x["weather"][0]["id"] for x in weather_12hours_next_data]
if len([x for x in lst_weather_code if x < 700]) > 0:
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Troi se mua ngay hom nay. Khi ra ngoai nho mang theo o ☂ boss nhe",
                        from_='+16266997586',
                        to='+84397479959'
                    )
