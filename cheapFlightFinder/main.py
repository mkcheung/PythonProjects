#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from dotenv import load_dotenv
from flight_search import FlightSearch
import os
import requests

load_dotenv()
AUTHENTICATIONTOKEN = os.getenv('SHEETY_AUTHENTICATION')

headers = {
    'Authorization': 'Basic '+ AUTHENTICATIONTOKEN,
}
sheetyApiEndpoint = "https://api.sheety.co/068202871558ae85a917dd6280a42997/flightDeals/prices"
response = requests.get(sheetyApiEndpoint, headers=headers)

sheet_data = response.json()
flightSearch = FlightSearch()
dataManager = DataManager()
for entry in sheet_data['prices']:
    if entry['iataCode'] == '':
        iataCode = flightSearch.process(cityName=entry['city'])
        entry['iataCode'] = iataCode
        flightSearch.flightsFromOrigin("LON", entry)
        dataManager.writeToSheet(entry)
    else:
        flightSearch.flightsFromOrigin("LON", entry)
        dataManager.writeToSheet(entry)


