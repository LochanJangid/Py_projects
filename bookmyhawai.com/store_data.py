import json

with open('flights_info.json', "a") as f:
    flight_data = input('Enter new flight data: ')
    json.dump(flight_data, f)