# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import FlightData

notificationManager = NotificationManager()
flightData = FlightData()
dataManager = DataManager(flightData)
# dataManager.post_data()
flightSearch = FlightSearch(dataManager.get_data(), notificationManager)
flightSearch.search_flight()
