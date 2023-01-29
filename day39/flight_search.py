import requests
from datetime import date, timedelta
import os

from notification_manager import NotificationManager

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
KIWI_END_P = "https://api.tequila.kiwi.com/v2/search"
HEADERS = {
    "apikey": TEQUILA_API_KEY,
    "Content-Type": "application/json",
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self, flight_data, notification_manager: NotificationManager):
        self.flight_data = flight_data
        self.notification = notification_manager

    def search_flight(self):
        departure_city = "Vilnius"
        city_code = "VNO"
        tomorrow = (date.today() + timedelta(days=1)).strftime("%d/%m/%Y")
        days = int(input("How many days do you want the search to range for ?"))
        end_date = (date.today() + timedelta(days=days)).strftime("%d/%m/%Y")
        for data in self.flight_data["prices"]:
            params = {
                "fly_from": city_code,
                "fly_to": data["iataCode"],
                "date_from": tomorrow,
                "date_to": end_date,
            }
            response = requests.get(url=KIWI_END_P, params=params, headers=HEADERS)
            response.raise_for_status()
            price = response.json()["data"][0]["price"]
            if price < data["lowestPrice"]:
                text = f"Low Price Alert! Only ${price} to fly from {departure_city}-{city_code}" \
                       f" to {data['city']}-{data['iataCode']}, from {tomorrow} to {end_date}"
                self.notification.send_message(text)
