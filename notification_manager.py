import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

TWILLIO_SID = os.environ.get('TWILLIO_SID')
TWILLIO_AUTH_TOKEN = os.environ.get('TWILLIO_AUTH_TOKEN')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, sms_content):
        client = Client(TWILLIO_SID, TWILLIO_AUTH_TOKEN)
        message = client.messages.create(
            body = sms_content,
            from_= '+15074456521',
            to="+5584999533866"
        )
        print(message.sid)