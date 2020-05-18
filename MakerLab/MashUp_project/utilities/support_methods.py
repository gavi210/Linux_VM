#this class contains support methods for the other classes
import math
from random import randint

def compute_distance(position, position1):
  diff_lat = float(position['lat']) - float(position1['lat'])
  diff_lon = float(position['lon']) - float(position1['lon'])

  distance = math.sqrt(math.pow(diff_lat,2) + math.pow(diff_lon,2))

  return distance

def pressed_events(events):
    pressed_events = []
    for i in range(len(events)):
        if(events[i].action == 'pressed'):
            pressed_events.append(events[i])
    return pressed_events

def random_list(weather_stations):
    list_len = len(weather_stations)
    mixed_list = []

    #print(weather_stations)
    while (len(mixed_list) != list_len):
        index = randint(0, len(weather_stations) - 1)
        mixed_list.append(weather_stations.pop(index))

    return mixed_list
