import requests
SHEET_ENDPOINT= "https://api.sheety.co/8b6c843d0b5584ab3894f9aee99bd4ce/flightDeals/prices"
SHEET_ENDPOINT2 = "https://api.sheety.co/8b6c843d0b5584ab3894f9aee99bd4ce/flightDeals/users"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def get_sheet_data(self):
        self.response = requests.get(url=SHEET_ENDPOINT)
        self.sheet_data = (self.response.json())["prices"]
        return self.sheet_data

    def update_IATA_code(self, IATA_code, id):
        self.update_row_params = {
            "price":
                {"iataCode":IATA_code}
            }
        update_response = requests.put(url=f"{SHEET_ENDPOINT}/{id}",json=self.update_row_params)
        # print(update_response.text)

    def get_customer_info(self):
        self.response = requests.get(url=SHEET_ENDPOINT2)
        self.customer_data = (self.response.json())["users"]
        return self.customer_data









