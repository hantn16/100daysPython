import requests as req
from pprint import pprint
import os
SHEETY_ENDPOINT = "https://api.sheety.co/41635b52676d5df8a9f1efdecffef3cf/flightDeals"
SHEETY_AUTH_BEARER = os.environ.get('SHEETY_AUTH_BEARER')


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            "Authorization": SHEETY_AUTH_BEARER
        }

    def get_data(self):
        res = req.get(url=f"{SHEETY_ENDPOINT}/prices", headers=self.headers)
        return res.json()['prices']

    def update_data(self, id, data):
        body = {
            "price": data
        }
        res = req.put(url=f"{SHEETY_ENDPOINT}/{id}",
                      headers=self.headers, json=body)
        return res.json()

    def get_emails(self):
        res = req.get(url=f"{SHEETY_ENDPOINT}/users", headers=self.headers)
        data = res.json()['users']
        return [x["email"] for x in data]
