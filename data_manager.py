import os
from dotenv import load_dotenv
import requests
load_dotenv()

SHEETY_API_KEY = os.environ.get('SHEETY_API_KEY')
SHEETY_AUTH = os.environ.get('SHEETY_AUTH')
SHEETY_APP_ID = os.environ.get('SHEETY_APP_ID')
SHEETY_GET_ENDPOINT = os.environ.get('SHEETY_GET_ENDPOINT')


sheety_headers = {
    'x-app-id': SHEETY_APP_ID,
    'x-app-key': SHEETY_API_KEY,
    'Authorization': SHEETY_AUTH
    }

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def get_flight_data(self):
        response = requests.get(url=SHEETY_GET_ENDPOINT,headers=sheety_headers)
        sheet_data = response.json()['prices']
        return sheet_data
    
    def update_flight_data(self,flight):
        flight_params = {
        'price':{
        'city':flight['city'],
        'iataCode':flight['iataCode'],
        'lowestPrice':flight['lowestPrice'],
        }
    }
        response = requests.put(url=f"{SHEETY_GET_ENDPOINT}/{flight['id']}", json=flight_params, headers=sheety_headers)
        print(response.text)
