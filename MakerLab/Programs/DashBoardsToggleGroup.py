from sense_emu import SenseHat
from time import sleep
from Adafruit_IO import Client, Feed, RequestError, Data
from AdafruitLogIn import username, key

#client object
aio = Client(username, key)

#senseHat
sense = SenseHat()

#list of the feeds connected to the dashboards
feed_list = ['redled', 'greenled', 'blueled', 'yellowled']

#create a map that maps the feed_key to the correspondent color
feed_color = {'redled' : 'red', 'greenled' : 'green', 'yellowled' : 'yellow', 'blueled' : 'blue'}

colors = {'red' : (255,0,0), 'blue' : (0,0,255), 'green' : (0,255,0), 'yellow' : (0,255,255)}

color_conversion = {}
for name in feed_list:
    matrix_name = name[:-3] #remove ending 'led'
    color_conversion[name] = matrix_name + 'matrix'

#map containging as key the color and as value the feed corresponding to that color
feeds = {}

for feed in feed_list:
    try:
        feeds[feed_color[feed]] = aio.feeds(feed)
    except RequestError:
        feeds[feed_color[feed]] = aio.create_feed(Feed(name=feed,key=feed,history=True))

def show_color(color):
    for i in range(8):
        for j in range(8):
            sense.set_pixel(i,j, colors[color])
        sleep(0.1)

def get_active_feed():
    activeFeed = {}
    for feed in feed_list:
        value = aio.receive(feed).value
        activeFeed[feed] = value
    return activeFeed

def show_active_colors(active_feeds):
    for active in active_feeds:
        if(active_feeds[active] == 'ON'):
            show_color(feed_color[active])
        else:
            pass

while True:
    sense.clear()
    try:
        active_feeds = get_active_feed()
        print(active_feeds)
        show_active_colors(active_feeds)
        sleep(0.1)
        sense.clear()
    except KeyboardInterrupt:
        sense.clear()
        break