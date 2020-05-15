#this class used to retrieve a better place in which to be -> higher temperature -> better place
from retriever import get_weather_stations, get_specific_station
from random import choice

def get_temperature_emu(sense):
  current_temperature = sense.get_temperature()

  return current_temperature

def better_place(current_temperature):
  weather_stations = get_weather_stations()

  possibilities = []
  for weather_station in weather_stations:
    items = get_specific_station(weather_station)
    not_contains = bool(items['items'] == [])

    if(not_contains):
      pass
    else:
      temperature = items[0]['ambient_temp']
      if (temperature > current_temperature):
        possibilities.append(weather_station)
      else:
        pass
  return choice(possibilities)