# this class contains the methods for asking Google speech service to play the instructions audio
from pygame import mixer
import os
from gtts import gTTS

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

#function for creating the descrption file audio
def create_audio():
    os.chdir('audio')

    # text = 'Pull the joystick UP for the weather conditions under the ISS space station. Pull down for see the magic!'
    text = 'The nearest weather station is not currently working'
    text_audio = gTTS(text=text, lang='en')
    text_audio.save('not_working.mp3')
    os.chdir('.')

create_audio()