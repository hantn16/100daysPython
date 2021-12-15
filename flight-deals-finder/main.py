# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


def update_iataCode():
    dm = DataManager()
    sheet_data = dm.get_data()
    fs = FlightSearch()
    update_data = [{
        "city": x["city"],
        "iataCode":fs.get_iata_code(x["city"]),
        "id":x["id"],
        "lowestPrice":x["lowestPrice"],
    } for x in sheet_data if x["iataCode"] == ""]
    if len(update_data) > 0:
        for item in update_data:
            dm.update_data(item["id"], item)


def check_flight():
    dm = DataManager()
    sheet_data = dm.get_data()
    fs = FlightSearch()
    nm = NotificationManager()
    for item in sheet_data:
        fl = fs.get_cheapiest_flight(item["iataCode"])
        if fl and fl.price < item["lowestPrice"]:
            msg = f"Low price alert! Only £{fl.price} to fly from {fl.origin_city}-{fl.origin_airport} to {fl.departure_city}-{fl.departure_airport}, from {fl.out_date} to {fl.return_date}"
            print(msg)
            nm.send_twilio_message(msg)


def main():
    update_iataCode()
    check_flight()


if __name__ == '__main__':
    main()
