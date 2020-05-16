#this is the main classmethod
from sense_emu import SenseHat
from description_audio import create_audio, play_audio, play_up, play_down
from support_methods import pressed_events
from pygame import mixer
import time

sense = SenseHat()
mixer.init()

#in an infinite loop checks every second if events occurs...
#if yes, looks for which are type 'pressed'
while True:
    try:
        events = sense.stick.get_events()
        events = pressed_events(events)

        for event in events:
            if(event.direction == 'up'):
                play_up(mixer)
            elif(event.direction == 'middle'):
                play_audio('functionalities', mixer)
            elif(event.direction == 'down'):
                play_down(mixer, sense)
        #play_audio('functionalities', mixer)
    except KeyboardInterrupt:
        sense.clear()
        while mixer.music.get_busy():
            pass
        create_audio('Bye Bye', 'bye')
        play_audio('bye', mixer)
        print('Bye Bye')
        break