import requests
import os

KIWI_LOCATION_ENDP = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
HEADERS = {
    "apikey": TEQUILA_API_KEY,
    "Content-Type": "application/json",
}


class FlightData:

    def __init__(self):
        self.data = []

    def get_city_code(self, city_name):
        location_params = {
            "term": city_name,
        }
        response = requests.get(url=KIWI_LOCATION_ENDP, params=location_params, headers=HEADERS)
        response.raise_for_status()
        city_code = response.json()["locations"][0]["code"]
        return city_code

    def set_flight_data(self):
        count = int(input("How many cities would you like to add? "))
        print("Enter the name of cities you would like to add to your flight data and the max price you want to set")
        while count > 0:
            city_name = input("\n\nEnter city name: ").title()
            city_code = self.get_city_code(city_name)
            flight_info = {"city": city_name,
                           "iataCode": city_code,
                           "lowestPrice": int(input("Enter max price: $")), }
            self.data.append(flight_info)
            count -= 1
