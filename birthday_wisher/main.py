import smtplib
import datetime as dt
import random
import pandas as pd
my_email = "hantn.devx@gmail.com"
password = "hanoilahan16"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="hantn.ntl@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of the email")
# current_date = dt.datetime.now()
# week_day = dt.datetime.weekday(current_date)
# if week_day == 5:
#     with open("./birthday_wisher/quotes.txt") as file:
#         lst_quotes = file.readlines()
#         quote = random.choice(lst_quotes)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email, to_addrs="hantn.ntl@gmail.com", msg=f"Subject:Monday Motivation\n\n{quote}")
##################### Extra Hard Starting Project ######################


def send_mail(to_addrs, subject, content):
    try:
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=my_email, password=password)
            conn.sendmail(from_addr=my_email, to_addrs=to_addrs,
                          msg=f"Subject:{subject}\n\n{content}")
        return True
    except Exception:
        return False


# 1. Update the birthdays.csv
data = pd.read_csv("./birthday_wisher/birthdays.csv")
lst = data.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
day = dt.datetime.now().day
month = dt.datetime.now().month
my_lst = [(x['name'], x['email'])
          for x in lst if x['day'] == day and x['month'] == month]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(my_lst) > 0:
    for item in my_lst:
        with open(f"./birthday_wisher/letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            content = letter.read().replace('[NAME]', item[0])
        send_mail(item[1], "Happy Birth Day", content)
# 4. Send the letter generated in step 3 to that person's email address.
