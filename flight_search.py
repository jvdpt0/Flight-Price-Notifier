import os
from dotenv import load_dotenv
import requests
from flight_data import FlightData
load_dotenv()

KIWI_API_KEY = os.environ.get('KIWI_API_KEY')
KIWI_ENDPOINT = 'https://api.tequila.kiwi.com/'

kiwi_headers = {
    'apikey':KIWI_API_KEY
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def check_iata_code(self,flight_data):
        if flight_data['iataCode'] == '':
            params = {
                'term':flight_data['city'],
                'location_types':'city',
                'limit':'1'
            }
            response = requests.get(url = f'{KIWI_ENDPOINT}locations/query',params=params, headers=kiwi_headers)
            city_data = response.json()['locations']
            code = city_data[0]['code']
            return code
        
    def flight_data_search(self,citycode):
        params = {
            'fly_from': 'NAT',
            'fly_to': citycode,
            'date_from':'03/11/2023',
            'date_to':'03/11/2023',
            'curr':'BRL'
        }
        response = requests.get(url=f'{KIWI_ENDPOINT}v2/search', params=params, headers=kiwi_headers,)
        data = response.json()['data'][0]
        flight_data = FlightData(
            price = data['price'],
            origin_city=data['cityFrom'],
            origin_airport= data['route'][0]['flyFrom'],
            destination_city = data['cityTo'],
            destination_airport= data['route'][1]['flyTo'],
            out_date = data['route'][0]['local_departure'].split('T')[0],
            return_date = data['route'][1]['local_arrival'].split('T')[0]
        )
        print(f"{flight_data.destination_city}: R${flight_data.price}")
        return flight_data


