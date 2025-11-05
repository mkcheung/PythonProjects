
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
import os
import requests

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv('AMADEUS_APIKEY')
        self.secret = os.getenv('AMADEUS_SECRET')
        self.apiTokenEndpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.cityEndpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.flightOfferEndpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.getToken()

    def getToken(self):
        parameters = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.secret,
        }
        response = requests.post(self.apiTokenEndpoint, data=parameters)
        response.raise_for_status()
        responseForToken = response.json()
        self.token = responseForToken['access_token']

    def process(self, cityName: str):
        headers = {"Authorization": f"Bearer {self.token}"}
        parameters = {
            "keyword": cityName,
            "include": "AIRPORTS",
        }
        response = requests.get(self.cityEndpoint, params=parameters, headers=headers)
        response.raise_for_status()
        responseForCity = response.json()
        return responseForCity['data'][0]['iataCode']

    def flightsFromOrigin(self, origin: str, entry:dict):
        headers = {"Authorization": f"Bearer {self.token}"}
        today = date.today()
        tomorrow = today + timedelta(days=1);
        parameters = {
            "originLocationCode": origin,
            "destinationLocationCode": entry['iataCode'],
            "departureDate": tomorrow.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
        }
        response = requests.get(self.flightOfferEndpoint, params=parameters, headers=headers)
        response.raise_for_status()
        responseToLocations = response.json()
        cheapestFare = self.find_cheapest_flight(responseToLocations['data'])
        if cheapestFare < float(entry['lowestPrice']):
            entry['lowestPrice'] = cheapestFare

    def find_cheapest_flight(self, data):
        cheapestFare = 9999999.0
        for flight in data:
            total = float(flight['price']['total'])
            if total < cheapestFare:
                cheapestFare = total
        return cheapestFare