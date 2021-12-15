class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, origin_city, origin_city_code, origin_airport, departure_airport, departure_city, departure_city_code, price, out_date, return_date):
        self.origin_city = origin_city
        self.origin_city_code = origin_city_code
        self.origin_airport = origin_airport
        self.departure_airport = departure_airport
        self.departure_city = departure_city
        self.departure_city_code = departure_city_code
        self.out_date = out_date
        self.return_date = return_date
        self.price = price
