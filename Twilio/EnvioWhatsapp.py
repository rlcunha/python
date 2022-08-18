
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Your Account SID from twilio.com/console
account_sid = "ACd290f58b5d8d01046bc18d7b470a5fc7"
# Your Auth Token from twilio.com/console
auth_token = "d5117ae1235b8349b7681c314017efef"

print(account_sid)
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Oi teste?',
    from_='whatsapp:+14155238886',
    to='whatsapp:+5511998571355'
)

print(message.sid)
