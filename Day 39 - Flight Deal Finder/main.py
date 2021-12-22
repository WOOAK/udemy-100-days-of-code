#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from date import Date
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
print(sheet_data)
flight_search = FlightSearch()
date = Date()
start_date, end_date = date.get_date()
notification_manager = NotificationManager()
DEPARTURE_CITY_NAME = "London"

for city in range(len(sheet_data)):
    iata_code = sheet_data[city]["iataCode"]
    arrival_city = sheet_data[city]["city"]
    id_count = sheet_data[city]["id"]
    lowest_price = sheet_data[city]["lowestPrice"]
    if iata_code == "":
        iata_code = flight_search.get_IATA_code(arrival_city)
        data_manager.update_IATA_code(iata_code,id_count)
    flight = flight_search.cheapest_flight(iata_code,start_date,end_date)
    # print(flight)
    if flight:
        if flight.price <= lowest_price:
            notification_manager.send_WA(flight.price, DEPARTURE_CITY_NAME,flight.dep_airport,arrival_city,flight.arr_airport,flight.go_date,flight.return_date,flight.link)


