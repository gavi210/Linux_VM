# this class contains the methods for asking Google speech service to play the instructions audio
from pygame import mixer
import os
from gtts import gTTS

def play_name(file):
  #play the audio
  mixer.init()
  mixer.music.load(file)
  mixer.music.play()

  #while it it busy, wait
  while mixer.music.get_busy() == True:
    pass

def get_source(name):
  #change working directory in oredr to get the description file audio
  os.chdir('audio')
  
  mixer.init()
  audio_file = mixer.load(name + '.mp3')

  #change back the working directory
  os.chdir('.')

  return audio_file
  
#function for creating the descrption file audio
def create_audio():
    os.chdir('audio')

    # text = 'Pull the joystick UP for the weather conditions under the ISS space station. Pull down for see the magic!'
    text = 'The nearest weather station is not currently working'
    text_audio = gTTS(text=text, lang='en')
    text_audio.save('not_working.mp3')
    os.chdir('.')

def better_location_name(name):
  os.chdir('audio')

  text = 'Based on the temperature, you\'ll stay better at' + name
  text_audio = gTTS(text=text, lang='en')

  #return a file audio to be played

#create_audio()