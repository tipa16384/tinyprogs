import requests
import json

noaa_api_url = 'https://api.weather.gov/'
user_agent_string = 'TerraBot/1.0'

latitude = 41.765
longitude = -72.5125
grid_identifier = None
location_name = None
zone_id = None
radar_station = None

headers = {'User-Agent': user_agent_string, 'Accept': 'application/geo+json'}

def get_location_information():
    global grid_identifier, location_name, zone_id, radar_station

    url = noaa_api_url + 'zones'
    parameters = {'point': str(latitude) + ',' + str(longitude), 'type': 'forecast', 'include_geometry': 'true'}
    response = requests.get(url, headers=headers, params=parameters)
    properties = response.json()['features'][0]['properties']
    grid_identifier = properties['gridIdentifier']
    location_name = properties['name']
    zone_id = properties['id']
    radar_station = properties['radarStation']

def get_forecast():
    url = noaa_api_url + 'zones/land/' + zone_id + '/forecast'
    response = requests.get(url, headers=headers)
    forecast = response.json()['properties']['periods']
    return forecast

def print_location_information():
    # print the location information
    print('Location Information')
    print('---------------------')
    print('Grid Identifier: ' + grid_identifier)
    print('Location Name: ' + location_name)
    print('Zone ID: ' + zone_id)
    print('Radar Station: ' + radar_station)

if __name__ == '__main__':
    get_location_information()
    print_location_information()
    forecast = get_forecast()
    for f in forecast:
        print(f['name'] + ': ' + f['detailedForecast'])
        print('')
