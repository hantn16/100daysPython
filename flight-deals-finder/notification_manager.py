from twilio.rest import Client
import os
TWILIO_ACCOUNT_SID = "ACf05e4ecd2e28e38f0a6602cea4931e19"


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
