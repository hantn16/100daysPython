from twilio.rest import Client
import os
import smtplib
TWILIO_ACCOUNT_SID = "ACf05e4ecd2e28e38f0a6602cea4931e19"
my_email = "hantn.devx@gmail.com"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_twilio_message(self, message):
        account_sid = TWILIO_ACCOUNT_SID
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        print(auth_token)
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=message,
            from_='+16266997586',
            to='+84397479959'
        )

    def send_emails(self, lst_address, subject, content):

        gmail_password = os.environ.get('GMAIL_PASSWORD')
        print(gmail_password)
        encoded_content = content.encode('UTF-8')
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=my_email, password=gmail_password)
            conn.sendmail(from_addr=my_email, to_addrs=lst_address,
                          msg=f"Subject:{subject}\n\n{encoded_content}")
