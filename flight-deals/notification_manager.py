import os

from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_ID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("VIRTUAL_PHONE_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("PHONE_NUMBER")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)