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

def nearest_pi(position):
  url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

  response = urllib.request.urlopen(url)

  result = json.loads(response.read())
  result = result['items']
  
  min_distance = -1
  closest_weather_station = None
  for weather_station in result:
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
  url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements'
  id = closest_weather_station['weather_stn_id']

  url = url + '/' + str(id)

  response = urllib.request.urlopen(url)

  result = json.loads(response.read())
  
  #check if the list is empty 
  contains = bool(result['items'] == [])

  if(not contains): 
     

  print(result)

dictionary = get_iss_position()
closest_weather_station = nearest_pi(dictionary)
retrieve_weather(closest_weather_station)