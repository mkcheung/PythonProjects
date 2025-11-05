from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()
AUTHENTICATIONTOKEN = os.getenv('SHEETY_AUTHENTICATION')

class DataManager:
    def __init__(self):
        self.sheetyApiEndpoint = "https://api.sheety.co/068202871558ae85a917dd6280a42997/flightDeals/prices"
   
    def writeToSheet(self, dictToUpdate:dict):

        headers = {
            'Authorization': 'Basic '+ AUTHENTICATIONTOKEN,
        }
        rowId = dictToUpdate['id']
        rowToUpdateUrl = f"{self.sheetyApiEndpoint}/{rowId}"
        parameters = {
            "price": dictToUpdate
        }
        response = requests.put(rowToUpdateUrl, json=parameters, headers=headers)
        response.raise_for_status()