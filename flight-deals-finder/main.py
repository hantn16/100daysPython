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
    emails = dm.get_emails()
    print(emails)
    fs = FlightSearch()
    nm = NotificationManager()
    for item in sheet_data:
        fl = fs.get_cheapiest_flight(item["iataCode"])
        if fl == None:
            fl = fs.get_cheapiest_flight(item["iataCode"], max_stopovers=1)
            if fl == None:
                print("No flight found")
                continue
        if fl.price < item["lowestPrice"]:
            template = "Low price alert! Only £{0} to fly from {1}-{2} to {3}-{4}, from {5} to {6}. {7}"
            stopover_msg = f"Flight has 1 stop over, via {fl.stopover_city}" if fl.stopover_city != None else ""
            msg = template.format(fl.price, fl.origin_city, fl.origin_airport, fl.departure_city,
                                  fl.departure_airport, fl.out_date, fl.return_date, stopover_msg)
            print(msg)
            link = f"https://www.google.co.uk/flights?hl=en#flt={fl.origin_airport}.{fl.departure_airport}.{fl.out_date}*{fl.departure_airport}.{fl.origin_airport}.{fl.return_date}"
            # msg = f"Low price alert! Only £{fl.price} to fly from {fl.origin_city}-{fl.origin_airport} to {fl.departure_city}-{fl.departure_airport}, from {fl.out_date} to {fl.return_date}"
            # nm.send_twilio_message(msg)
            subject = "New Low Price Flight"
            nm.send_emails(lst_address=emails, subject=subject,
                           content=f"{msg}\n{link}")


def main():
    update_iataCode()
    check_flight()


if __name__ == '__main__':
    main()
