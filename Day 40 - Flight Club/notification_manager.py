from twilio.rest import Client
import smtplib

ACCOUNT_SID = "AC77b240fca3f56d154ed8678144255a93"
AUTH_TOKEN = "324e8049e647639df2ceb745684ab07d"
FROM_WHATSAPP_NUMBER = 'whatsapp:+14155238886'
TO_WHATSAPP_NUMBER = 'whatsapp:+601137837026'
MY_EMAIL = "killer_1021@hotmail.com"
EMAIL_PASSWORD = "Kuan1120//"
EMAIL_SUBJECT = "Low Price Alert from Junin's Flight Club!"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        super().__init__()
        self.client=Client(ACCOUNT_SID,AUTH_TOKEN)

    def send_WA(self,price,departure_city_name,departure_airport,arrival_city,arrival_airport,go_date,return_date,link,stop_overs,via_city):
        self.message = f"Low price alert! Only £{price} to fly from {departure_city_name}-{departure_airport} to {arrival_city}-{arrival_airport}, from {go_date} to {return_date}. For more details, kindly visit {link}"
        if stop_overs > 0:
            self.message += f"\nFlight has {stop_overs} stop over, via {via_city}"
        self.client.messages.create(body=self.message,
                               from_=FROM_WHATSAPP_NUMBER,
                               to=TO_WHATSAPP_NUMBER)
    def send_email(self,name, email, price,departure_city_name,departure_airport,arrival_city,arrival_airport,go_date,return_date,stop_overs,via_city):
        connection = smtplib.SMTP("smtp-mail.outlook.com",587)
        connection.starttls()
        connection.login(user=MY_EMAIL,password=EMAIL_PASSWORD)
        google_flight_link = f"https://www.google.co.uk/flights?hl=en#flt={departure_airport}.{arrival_airport}.{go_date}*{arrival_airport}.{departure_airport}.{return_date}"
        message = f"Dear {name},\n"
        message += f"Low price alert! Only £{price} to fly from {departure_city_name}-{departure_airport} to {arrival_city}-{arrival_airport}, from {go_date} to {return_date}. For more details, kindly visit {google_flight_link}"
        if stop_overs > 0:
            message += f"\nFlight has {stop_overs} stop over, via {via_city}"
        print(message)
        content = "From: %s\r\n" % MY_EMAIL + "To: %s\r\n" % email + "Subject: %s\r\n" % EMAIL_SUBJECT + "\r\n" + message
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=content.encode('utf-8'))

