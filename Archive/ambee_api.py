#!/usr/bin/python3

from configparser import ConfigParser
import urllib.request as request
import sys as system
from time import sleep
import json

def print_results(query):
    data = query[0]
    print('\n---------- Location Data ----------\n')
    print(f'State: {data["state"]}')
    print(f'Divison: {data["division"]}')
    print(f'City: {data["city"]}')
    print(f'Address: {data["placeName"]}')
    print('\n---------- Environmental Metrics ----------\n')
    print(f'Air Quality Index (AQI): {data["AQI"]}')
    print(f'- AQI Pollutant: {data["aqiInfo"]["pollutant"]}')
    print(f'- AQI Pollutant Concentration: {data["aqiInfo"]["concentration"]}')
    print(f'- AQI Concentration Category: {data["aqiInfo"]["category"]}')
    print(f'Carbon Monoxide (CO): {data["CO"]}')
    print(f'Nitrogen Dioxide (NO2): {data["NO2"]}')
    print(f'Ozone (O3): {data["OZONE"]}')
    print(f'Sulfer Dioxide (SO2): {data["SO2"]}')
    print(f'Particulate Matter 10 (PM10): {data["PM10"]}')
    print(f'Particulate Matter 25 (PM25): {data["PM25"]}')



check = input('\n>>> Are you sure you want to query for Ambee Forest Fire data? (100 Calls/Day). Type \'y\' or \'yes\' to confirm: ')
if (check != 'y' and check != 'yes'):
    print('>>> Aborting Ambee API Call')
    system.exit()

print('\n>>> Querying Ambee API...\n')

# API Key
print('>>> Obtaining API Key Locally...')
sleep(2.0)

config = ConfigParser()
config.read('config.ini')
try:
    key = config['API']['KEY']
except:
    print('\n>>> No local API Key found. Aborting...')
    system.exit()

# Spokane Coordiantes
lat = 47.668331
long = -117.402771

# South of Kennewick Fire
lat = 45.880782
long = -119.167000

# obtain query type -> known: latest, forecast
type_check = ''
while (type_check != 'fire' and type_check != 'general'):
    type_check = input('\n>>> Forest Fire Info or General Location Info? (\'fire\', \'general\'): ')

query_type = ''

while (query_type != 'latest' and query_type != 'forecast'):
    query_type = input('\n>>> What kind of information are you querying? (\'latest\', \'forecast\'): ')

fire = f'fire/v2/{query_type}/by-lat-lng'
normal = f'weather/{query_type}/by-lat-lng'

query = ''
if (type_check == 'fire'):
    query = fire
else:
    query = normal 


print(f'\n>>> Attempting to Query {type_check} data from https://api.ambeedata.com/...')
sleep(2.0)

# sample = b'{"message":"success","stations":[{"CO":0.153,"NO2":5.722,"OZONE":28.03,"PM10":9.361,"PM25":3.17,"SO2":1.288,"city":"Spokane","countryCode":"US","division":"Spokane","lat":47.64999999999219,"lng":-117.39999999998577,"placeName":"E Hartson Ave","postalCode":"99202-2334","state":"Washington","updatedAt":"2023-10-11T19:00:00.000Z","AQI":26,"aqiInfo":{"pollutant":"O3","concentration":28.03,"category":"Good"}}]}'
# with open('ambee_general.json', 'w') as fun:
#         json.dump(json.loads(sample)['stations'], fun, indent=3)

url = f"https://api.ambeedata.com/{query}?lat={lat}&lng={long}"
header = {'x-api-key' : key}

# json format result in byte
request_api = request.Request(url=url, headers=header)
response_api = request.urlopen(request_api)

# format received byte string data
print('\n>>> Formatting Data...\n')
sleep(2.0)
data = response_api.read()
json_data = json.loads(data)
print(data)

if (type_check == 'fire'):
    print(f'\n{data}\n')
    with open('ambee_fire_forecast.json', 'w') as fun:
        json.dump(json_data, fun, indent=3)
    # print(json.dumps(json.loads(response_api.read()), indent=3)) -> not working right now
else:
    if (type_check == 'general' and query_type == 'latest'):
        print_results(json_data['stations'])
    # write to .json
    with open('ambee_general.json', 'w') as fun:
        json.dump(json_data, fun, indent=3)