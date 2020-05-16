# this class contains the methods for retrieving current position of the Iss (lan,lon)
# and for retrieving from the weather application of the nearest RaspBerry Pi

import urllib.request
import json
from support_methods import compute_distance

def get_iss_position():
  url = 'http://api.open-notify.org/iss-now.json'

  response = urllib.request.urlopen(url)

  result = json.loads(response.read())
  result = result['iss_position']
  position = {}
  position['lat'] = result['latitude']
  position['lon'] = result['longitude']

  #return a dictionaty with lat and long values
  return position

def get_weather_stations():
  url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

  response = urllib.request.urlopen(url)

  result = json.loads(response.read())
  result = result['items']
  return result

def get_specific_station(weather_station):
  url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements'
  id = weather_station['weather_stn_id']
  url = url + '/' + str(id)

  response = urllib.request.urlopen(url)

  result = json.loads(response.read())
  return result

def nearest_pi(position, stations_list):

  min_distance = -1
  closest_weather_station = None
  for weather_station in stations_list:
    position1 = {}
    position1['lat'] = weather_station['weather_stn_lat']
    position1['lon'] = weather_station['weather_stn_long']

    if(min_distance == -1): #first time in the loop
      min_distance = compute_distance(position, position1)
      closest_weather_station = weather_station
    else:
      possible_min = compute_distance(position, position1)
      if(possible_min < min_distance and possible_min > 0):
        min_distance = possible_min
        closest_weather_station = weather_station
  return closest_weather_station

def retrieve_weather(closest_weather_station):
  result = get_specific_station(closest_weather_station)

  #check if the list is empty
  not_contains = bool(result['items'] == [])

  if(not_contains):
    return -1
  else:
    print(result)
    result = result['items'][0]
    weather_description = 'The nearest weather station is ' + result['created_by'] + '. The temperature: ' + str(result['ambient_temp']) + ' degrees'
    return weather_description



