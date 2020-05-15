# this class contains the methods for asking Google speech service to play the instructions audio
from pygame import mixer
import os

def play_instructions():

  #change working directory in oredr to get the description file audio
  os.chdir('audio')

  #play the audio
  mixer.init()
  mixer.music.load('functionalities.mp3')
  mixer.music.play()

  #while it it busy, wait
  while mixer.music.get_busy() == True:
    pass

  #change back the working directory
  os.chdir('.')
