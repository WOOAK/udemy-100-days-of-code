class FlightData:
    #This class is responsible for structuring the flight data.
    #
    def __init__(self,price,dep_airport,arr_airport,link,go_date,return_date,stop_overs = 0, via_city = ""):
        self.price = price
        self.dep_airport = dep_airport
        self.arr_airport = arr_airport
        self.link = link
        self.go_date = go_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city

