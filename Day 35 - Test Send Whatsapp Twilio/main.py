from twilio.rest import Client

account_sid = "AC77b240fca3f56d154ed8678144255a93"
auth_token = "324e8049e647639df2ceb745684ab07d"
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(account_sid, auth_token)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+601137837026'

client.messages.create(body='Hi I know your name',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)