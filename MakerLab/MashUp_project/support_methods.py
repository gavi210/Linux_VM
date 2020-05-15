#this class contains support methods for the other classes
import math

def compute_distance(position, position1):
  diff_lat = float(position['lat']) - float(position1['lat'])
  diff_lon = float(position['lon']) - float(position1['lon'])

  distance = math.sqrt(math.pow(diff_lat,2) + math.pow(diff_lon,2))

  return distance 