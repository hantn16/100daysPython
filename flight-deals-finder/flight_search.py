from pprint import pprint
import os
import requests as req
from datetime import datetime, timedelta
from flight_data import FlightData
TEQUILA_APIKEY = os.environ.get('TEQUILA_APIKEY')
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TIME_DELTA = 6 * 30
MINLENGTH_OF_STAYIN = 7
MAXLENGTH_OF_STAYIN = 28


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            "apikey": TEQUILA_APIKEY
        }

    def get_iata_code(self, city: str):
        url = f"{TEQUILA_ENDPOINT}/locations/query"
        params = {
            "term": city,
            "location_types": "city",
            "locale": "en-US",
            "limit": 5
        }
        res = req.get(url=url, params=params, headers=self.headers)
        data = res.json()
        return data["locations"][0]["code"]

    def get_cheapiest_flight(self, to_city, from_city="LON", max_stopovers=0):
        url = f"{TEQUILA_ENDPOINT}/v2/search"
        date_from = datetime.now() + timedelta(days=1)
        date_to = datetime.now() + timedelta(days=TIME_DELTA)
        params = {
            "fly_from": f"city:{from_city}",
            "fly_to": f"city:{to_city}",
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": MINLENGTH_OF_STAYIN,
            "nights_in_dst_to": MAXLENGTH_OF_STAYIN,
            "curr": "GBP",
            "max_stopovers": max_stopovers,
            "one_for_city": 1,
            "flight_type": "round"
        }
        res = req.get(url=url, params=params, headers=self.headers)
        try:
            res_data = res.json()["data"][0]
            routes = res_data["route"]
            stopover_city_list = [x["cityTo"] for x in routes if x["cityTo"] !=
                                  res_data["cityFrom"] and x["cityTo"] != res_data["cityTo"]]
            flight_data = FlightData(
                origin_city=res_data["cityFrom"],
                origin_city_code=res_data["cityCodeFrom"],
                origin_airport=res_data["flyFrom"],
                departure_city=res_data["cityTo"],
                departure_city_code=res_data["cityCodeTo"],
                departure_airport=res_data["flyTo"],
                info_link=res_data["deep_link"],
                stopover_city=", ".join(stopover_city_list) if len(
                    stopover_city_list) > 0 else None,
                price=res_data["price"],
                out_date=res_data["route"][0]["local_departure"].split("T")[0],
                return_date=res_data["route"][1]["local_departure"].split("T")[
                    0],
            )
            print(f"{flight_data.departure_city}: £{flight_data.price}")
            return flight_data
        except IndexError:
            return None
