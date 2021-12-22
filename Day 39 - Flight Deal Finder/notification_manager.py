from twilio.rest import Client

ACCOUNT_SID = "AC77b240fca3f56d154ed8678144255a93"
AUTH_TOKEN = "324e8049e647639df2ceb745684ab07d"
FROM_WHATSAPP_NUMBER = 'whatsapp:+14155238886'
TO_WHATSAPP_NUMBER = 'whatsapp:+601137837026'
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        super().__init__()
        self.client=Client(ACCOUNT_SID,AUTH_TOKEN)

    def send_WA(self,price,departure_city_name,departure_airport,arrival_city,arrival_airport,go_date,return_date,link):
        self.message = f"Low price alert! Only £{price} to fly from {departure_city_name}-{departure_airport} to {arrival_city}-{arrival_airport}, from {go_date} to {return_date}. For more details, kindly visit {link}"
        self.client.messages.create(body=self.message,
                               from_=FROM_WHATSAPP_NUMBER,
                               to=TO_WHATSAPP_NUMBER)