# this class contains the methods for asking Google speech service to play the instructions audio
from pygame import mixer
import os
from gtts import gTTS
from retriever import get_iss_position, get_weather_stations, nearest_pi, retrieve_weather
from better_place import get_temperature_emu, better_place

def play_audio(file, mixer):
  os.chdir('audio')

  #play the audio
  #mixer.init()
  mixer.music.load(file + '.mp3')
  os.chdir('..')
  mixer.music.play()

  #while it it busy, wait
  while mixer.music.get_busy() == True:
    pass
  return

#function for creating the descrption file audio
def create_audio(text, file_name):
    os.chdir('audio')
    audio = gTTS(text=text, lang='en')
    audio.save(file_name + '.mp3')
    os.chdir('..')
    return

def better_location_name(name):
  text = 'Based on the temperature, you\'ll stay better at' + name
  return text

def play_up(mixer):
    dictionary = get_iss_position()
    stations_list = get_weather_stations()
    closest_weather_station = nearest_pi(dictionary, stations_list) #find the closest weather station
    output = retrieve_weather(closest_weather_station)

    create_audio(output, 'play_up')
    play_audio('play_up', mixer)
    return

def play_down(mixer, sense):
    current_temperature = get_temperature_emu(sense)
    text = better_place(current_temperature)

    create_audio(text, 'play_down')
    play_audio('play_down', mixer)
    return

#create_audio()