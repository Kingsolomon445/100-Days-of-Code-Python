
import requests
import os

from flight_data import FlightData

SHEETY_ENDP = "https://api.sheety.co/2e5a24157faf35a913235ea8279cbde8/flightDeals/prices"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, flight_data: FlightData):
        self.flight_data = flight_data  # an object for FlightData class

    def get_data(self):
        response = requests.get(url=SHEETY_ENDP, auth=(USERNAME, PASSWORD))
        response.raise_for_status()
        sheet_data = response.json()
        return sheet_data


    def post_data(self):
        self.flight_data.set_flight_data()  # collect data from user to post
        for data in self.flight_data.data:
            params = {
                "price": {key: value for key, value in data.items()}
            }
            response = requests.post(url=SHEETY_ENDP, json=params, auth=(USERNAME, PASSWORD))
            response.raise_for_status()
            print(response.text)





