#this class used to retrieve a better place in which to be -> higher temperature -> better place
from utilities.retriever import get_weather_stations, get_specific_station
from random import choice
from utilities.support_methods import random_list

def get_temperature_emu(sense):
  current_temperature = sense.get_temperature()

  return current_temperature

def better_place_method(current_temperature):
  weather_stations = get_weather_stations()
  weather_stations = random_list(weather_stations)

  description_station = {}
  #read the list randomly
  for weather_station in weather_stations:

    items = get_specific_station(weather_station)
    not_contains = bool(items['items'] == [])

    if(not_contains):
      pass
    else:
      temperature = items['items'][0]['ambient_temp']
      if (temperature > current_temperature):
        #add current description into the dictionaty
        description_station['general'] = weather_station
        description_station['specific'] = items['items']
        break
      else:
        pass

  output = 'You will stay better near ' + description_station['specific'][0]['created_by']
  difference = description_station['specific'][0]['ambient_temp'] - current_temperature
  output = output + '. Here the temperature is ' + "{:.2f}".format(difference) + ' degrees warmer'
  return output