from sense_emu import SenseHat
from time import sleep
from Adafruit_IO import Client, Data, Feed, RequestError

from AdafruitLogIn import username, key #import username and key for logging in into the AdafruitIo

#Client for communicate  with AdafruitIo
aio = Client(username, key)

#object of the senseEmu
sense = SenseHat()

#dictionary mapping string ('Up' 'Down'... ) to correspondent color
#UP -> blue DOWN -> green #RIGHT -> yellow LEFT -> red
sense_dict_color = {"up" : "blue", "down" : "green", "right" : "yellow", "left" : "red"}

feeds_keys = ['blueled', 'greenled', 'yellowled', 'redled']

feeds = {} #dictionary containing the feeds... containing feed objects

for feed_key in feeds_keys:
    color = feed_key[:-3] #remove the last 3 character word 'led'
    try:
        #try to access the feed with such a key name
        #eliminate led for generate the touple... key = color, and feeds object
        feeds[color] = aio.feeds(feed_key)
    except RequestError:
        #generate a NewFeed
        feeds[color] = aio.create_feed(Feed(name=feed_key,key=feed_key,history=True))

print(feeds)

#function for turning on the value of the matrix and the led in the dashborad
def turn_on(direction):
    color = ''
    color = sense_dict_color[direction] #get the color corresponding to the direction inserted
    if (color != ''):
       #turn on the dashboard -> will change color
       aio.send_data(feeds[color].key, 1)
    else:
        return

#function for turning off
def turn_off(direction):
    color = ''
    color = sense_dict_color[direction]
    if(color != ''):
        aio.send_data(feeds[color].key, 0)
    else:
        return

while True:
    #in the infinite loop
    try:
        for event in sense.stick.get_events():
            direction = event.direction
            if(direction in sense_dict_color) :
                if(event.action == 'pressed'):
                    turn_on(event.direction)
                elif(event.action == 'released'):
                    turn_off(event.direction)
            else:
                pass
    except KeyboardInterrupt:
        pass