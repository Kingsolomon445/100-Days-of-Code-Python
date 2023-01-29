from twilio.rest import Client
import os

TWILIO_ACCT_SID = os.environ.get("TWILIO_ACCT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
RECEIVER_PHONE_NUMBER = os.environ.get("RECEIVER_PHONE_NUMBER")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_message(self, text):
        client = Client(TWILIO_ACCT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(body=text, from_=TWILIO_PHONE_NUMBER, to=RECEIVER_PHONE_NUMBER)
