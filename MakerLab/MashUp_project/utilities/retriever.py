# this class contains the methods for retrieving current position of the Iss (lan,lon)
# and for retrieving from the weather application of the nearest RaspBerry Pi

import urllib.request
import json
from utilities.support_methods import compute_distance

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

def decreasing_distance_order(position, stations_list):
  #this method orders the list of weather stations based on the distance
  #map has as key the distance and as value the weather_station
  nearest_order = {}

  for weather_station in stations_list:
    position1 = {}
    position1['lat'] = weather_station['weather_stn_lat']
    position1['lon'] = weather_station['weather_stn_long']

    distance = compute_distance(position, position1)
    nearest_order[distance] = weather_station

  #return a list of touples (<distance>, <weather station>)
  return sorted(nearest_order.items())

def nearest_working(ordered_station_list):
    #method check and retrieve the nearest station that is currently working
    for (distance, weather_station) in ordered_station_list:
        station_description = get_specific_station(weather_station)
        not_contains = bool(station_description['items'] == [])

        if(not_contains):
            pass
        else:
            station_description = station_description['items'][0]
            weather_description = 'The nearest weather station is ' + station_description['created_by']
            weather_description += '. The temperature: ' + str("{:.2f}".format(station_description['ambient_temp'])) + ' degrees'
            return weather_description
    return 'No weather stations are currently working'