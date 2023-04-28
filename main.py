#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

DM = DataManager()
FS = FlightSearch()
NM = NotificationManager()

sheet_data = DM.get_flight_data()

for flight in sheet_data:
    if flight['iataCode'] == '':
        new_iata_code = FS.check_iata_code(flight)
        flight['iataCode'] = new_iata_code
        DM.update_flight_data(flight)
    else:
        flight_data = FS.flight_data_search(flight['iataCode'])
        if int(flight_data.price) < int(flight['lowestPrice']):
            NM.send_sms(f"Low price alert! Only R${flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport} from {flight_data.out_date} to {flight_data.return_date}")
