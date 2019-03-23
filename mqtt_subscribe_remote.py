# Necessary libraries and packages:
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
import time
import math
import numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
print("before importing")
#from outputter import generate_output

# defining constants to calculate the distance:
radius = 6371000
p = 0.017453292519943295
latdata, longdata = [], []
#url_lat = 18.6205882
#url_long = 73.7843121
print("Defined Constants")

# Configuring the PubNub connection:
pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-29e0c45e-724c-42ba-be7b-cb156fc74a03"
pnconfig.subscribe_key = "sub-c-f739ed7a-2afb-11e9-8c30-16f8bea0bbad"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)
print("PubNub setup")
# Listener to handle the subscription:
my_listener = SubscribeListener()
pubnub.add_listener(my_listener)

def self_loc()->(float, float):
    pubnub.subscribe().channels('Self_Loc').execute()
    #my_listener.wait_for_connect()
    print('Self Subscriber Configured !')
    print('_______________________')

    result = my_listener.wait_for_message_on('Self_Loc')
    print(result.message)

    result_message = repr(result.message)
        

    # Waiting for connection:
    if result.message == str("Connected !"):
        print("\nRemote device calliberated and ready for transmission !")
        print("_______________________________________________________")

    else:

        # Filtering the lat-long from received message:
        result_loc = result_message.split('_')
        result_lat = float(result_loc[0][1:])
        result_long = float(result_loc[1][:-1])
        return result_lat, result_long
    

fig = plt.figure()
plt.xlim(-10000, 10000)
plt.ylim(-10000, 10000)
plt.axhline(y=0, color='r')
plt.axvline(x=0, color='r')

plt.xlabel("Distance Units (meters)")
plt.ylabel("Distance Units (meters)")
plt.title("Trajectory of the other Device.")
xdata, ydata = [], []
graph, = plt.plot([], [], '-')


def animate(x, y):
    xdata.append(x)
    ydata.append(y)
    graph.set_data(xdata, ydata)
    return graph

def distance(x1, y1, x2, y2):
        # Calculating distance between two points using 'Haversine Formula'.
        # This formula calculates the distance "As a crow flies", which is the
        # shortest distance between two points on a spheroid.
        # HAVERSINE FORMULA ->
        # a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)      ---Angle.
        # c = 2 ⋅ atan2( √a, √(1−a) )                       ---Calculation.
        # d = Radius ⋅ c                                    ---Distance.
        #
        # [ Here, φ is latitude, λ is longitude ]
        
    relative_lat = x2 - x1
    relative_long = y2 - y1
    
    a = math.pow(math.sin((relative_lat / 2) * p), 2) + \
            math.cos(x2 * p) * math.cos(x1) * math.pow(math.sin((relative_long / 2) * p), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    
    return d

a,b = self_loc()
print("a = {0}".format(self_loc()[0]))
print("b = {0}".format(self_loc()[1]))
# Making the script run continuously
# Subscribing to the channel:
pubnub.subscribe().channels('ESIoT').execute()
my_listener.wait_for_connect()
print('Subscriber Configured !')
print('_______________________')

while True:


    print("Waiting for the other device .... ")
    # Listening for messages:
    result = my_listener.wait_for_message_on('ESIoT')
    print(result.message)

    result_message = repr(result.message)
        

    # Waiting for connection:
    if result.message == str("Connected !"):
        print("\nRemote device calliberated and ready for transmission !")
        print("_______________________________________________________")

    else:

        # Filtering the lat-long from received message:
        result_loc = result_message.split('_')
        result_lat = float(result_loc[0][1:])
        result_long = float(result_loc[1][:-1])
        print("Received LAT : {0}".format(result_lat))
        print("Received LONG : {0}".format(result_long))
        print("MY LAT - LONG : {0} , {1}".format(url_lat, url_long))
        print("______")

        # Calculating relative co-ordinates:
        relative_lat = result_lat - url_lat
        relative_long = result_long - url_long
        
        print("relative lat : " + str(relative_lat))
        print("relative long : " + str(relative_long))
        
        latdata.append(relative_lat)
        longdata.append(relative_long)

        d = distance(url_lat, url_long, result_lat, result_long)

        print("Distance = {0} meters.".format(d))
        print("_______________________")

        plot_lat = distance(url_lat, 0, result_lat, 0)
        plot_long = distance(url_long, 0, result_long, 0)

        if relative_lat < 0 :
            plot_lat = 0 - plot_lat

        if relative_long < 0 :
            plot_long = 0 - plot_long
       
        print("plot_long : " + str(plot_long))
        print("plot_lat : " + str(plot_lat))

        ani = FuncAnimation(fig, animate(plot_lat, plot_long), frames=10, interval=200)
        plt.draw()
        plt.pause(0.1)
        
        generate_output(plot_lat, plot_long)
        
