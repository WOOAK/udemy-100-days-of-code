import requests
from flight_data import FlightData

TEQUILA1_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA2_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQ_API_KEY = "baJTICHAXYbIQ39AKEUmgilcDSDNgAmT"
DEPARTURE_CITY = "LON"
DEPARTURE_CITY_NAME = "London"
CURRENCY = "GBP"


teq_header = {
    "apikey":TEQ_API_KEY
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_IATA_code(self, city_name):
        self.IATA_params = {
        "term":city_name
                 }
        self.location_dict = (requests.get(url=TEQUILA1_ENDPOINT,params = self.IATA_params,headers=teq_header).json())
        self.IATA_code = self.location_dict["locations"][0]["code"]
        return self.IATA_code

    def cheapest_flight(self,code,start_date,end_date):
        self.flight_search_parms = {
            "fly_from": DEPARTURE_CITY,
            "fly_to": code,
            "curr": CURRENCY,
            "date_from": start_date.strftime("%d/%m/%Y"),
            "date_to": end_date.strftime("%d/%m/%Y"),
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28
        }
        self.flight_data = (requests.get(url=TEQUILA2_ENDPOINT, params=self.flight_search_parms, headers=teq_header).json())
        print(self.flight_data)
        try:
            price = self.flight_data["data"][0]["conversion"]["GBP"]
            departure_airport = self.flight_data["data"][0]["route"][0]["flyFrom"]
            arrival_airport = self.flight_data["data"][0]["route"][0]["flyTo"]
            link = self.flight_data["data"][0]["deep_link"]
            go_date = self.flight_data["data"][0]["route"][0]["local_departure"].split("T")[0]
            return_date = self.flight_data["data"][0]["route"][1]["local_departure"].split("T")[0]
            flight_data = FlightData(price, departure_airport,arrival_airport,link,go_date,return_date)
            print(price)
            print(departure_airport)
            print(arrival_airport)
            print(link)
            print(go_date)
            print(return_date)
            return flight_data
        except IndexError:
            print(f"No flight available for {code}!")
            return False




