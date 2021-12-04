import requests
from datetime import datetime
import time
import smtplib
MY_LAT = 20.9084384  # Your latitude
MY_LONG = 107.0682782  # Your longitude
MY_EMAIL = "hantn.devx@gmail.com"
PASSWORD = "hanoilahan16"


def is_iss_overhead(args):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    return MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_str = data["results"]["sunrise"].split("+")[0]
    sunrise = datetime.strptime(sunrise_str, "%Y-%m-%dT%H:%M:%S")
    # sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    print(sunrise)
    sunset_str = data["results"]["sunset"].split("+")[0]
    sunset = datetime.strptime(sunset_str, "%Y-%m-%dT%H:%M:%S")
    # sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunset)
    time_now = datetime.utcnow()
    print(time_now)
    return not (sunset <= time_now <= sunrise)


def send_mail(to_addrs, subject, content):
    try:
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=PASSWORD)
            conn.sendmail(from_addr=MY_EMAIL, to_addrs=to_addrs,
                          msg=f"Subject:{subject}\n\n{content}")
        return True
    except Exception:
        return False


# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_mail(MY_EMAIL, "LookUp 🌌🪐🌍", "The ISS is above you in sky.")
