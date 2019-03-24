# Necessary libraries and packages:
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
import time
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from outputter import generate_output
from ui import UI
import threading

# defining constants to calculate the distance:
user_interface = UI()
radius = 6371000
p = 0.017453292519943295
latdata, longdata = [], []


# Function to update status on UI:
def update_status(stat):
    status_thread = threading.Thread(target=user_interface.set_status(stat))
    status_thread.start()


# Function to update self location on UI:
def update_our_loc(self_lat_var, self_long_var):
    self_loc_thread = threading.Thread(target=user_interface.set_our_location(self_lat_var, self_long_var))
    self_loc_thread.start()


# Function to update remote location on UI:
def update_remote_loc(remote_lat, remote_long):
    remote_loc_thread = threading.Thread(target=user_interface.set_remote_location(remote_lat, remote_long))
    remote_loc_thread.start()


# Function to update distance on UI:
def update_distance(distance_var):
    status_thread = threading.Thread(target=user_interface.set_distance(distance_var))
    status_thread.start()


# Function to send co-ordinates to the outputter file:
def send_to_outputter(lat, long):
    output_thread = threading.Thread(target=generate_output(lat, long))
    output_thread.start()


# Configuring the PubNub connection:
pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-29e0c45e-724c-42ba-be7b-cb156fc74a03"
pnconfig.subscribe_key = "sub-c-f739ed7a-2afb-11e9-8c30-16f8bea0bbad"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)
print("Connecting to PubNub MQTT Broker Service")
update_status("Connecting to PubNub MQTT Broker Service")
time.sleep(2)

# Listener to handle the subscription:
self_listener = SubscribeListener()
pubnub.add_listener(self_listener)

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


# Calculating distance between two points using 'Haversine Formula':
def distance(x1, y1, x2, y2):
        # This formula calculates the distance "As a crow flies", which is the
        # shortest distance between two points on a spheroid.
        # HAVERSINE FORMULA ->
        # a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)      ---Angle.
        # c = 2 ⋅ atan2( √a, √(1−a) )                       ---Calculation.
        # d = Radius ⋅ c                                    ---Distance.
        #
        # [ Here, φ is latitude, λ is longitude ]
        
    relative_latitude = x2 - x1
    relative_longitude = y2 - y1
    
    a = math.pow(math.sin((relative_latitude / 2) * p), 2) + \
            math.cos(x2 * p) * math.cos(x1) * math.pow(math.sin((relative_longitude / 2) * p), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    
    return d


# Function to acquire self location:
def self_loc()->(float, float):

    # Subscribing to the self channel:
    pubnub.subscribe().channels('Self_Loc').execute()
    self_listener.wait_for_connect()
    print('Subscriber configuration : 1/2 completed !')
    update_status('Subscriber configuration : 1/2 completed !')
    print('_______________________')

    # Getting current status:
    while True:
        self_result = self_listener.wait_for_message_on('Self_Loc')
        self_result_message: str = repr(self_result.message)

        if self_result.message == str('Connected !'):
            print('Receiving Location Data ...')
            update_status('Receiving Location Data ...')
            break

        else:
            print(self_result_message)
            update_status(self_result_message)
            continue

    # Getting current location:
    self_result = self_listener.wait_for_message_on('Self_Loc')
    self_result_message: str = repr(self_result.message)

    # Filtering the lat-long from received message:
    self_result_loc = self_result_message.split('_')
    self_result_lat = float(self_result_loc[0][1:])
    self_result_long = float(self_result_loc[1][:-1])
    pubnub.remove_listener(self_listener)
    return self_result_lat, self_result_long


# Acquiring location and updating UI:
self_lat, self_long = self_loc()
update_our_loc(self_lat, self_long)

# Subscribing to the remote channel:
remote_listener = SubscribeListener()
pubnub.add_listener(remote_listener)
pubnub.subscribe().channels('ESIoT').execute()
remote_listener.wait_for_connect()
print('Subscriber Configured !')
update_status('Subscriber Configured !')
print('_______________________')

# Making the script run continuously
while True:
    print("Waiting for the other device .... ")
    update_status('Waiting for the other device .... ')

    # Listening for messages:
    result = remote_listener.wait_for_message_on('ESIoT')
    print(result.message)

    result_message = repr(result.message)

    # Waiting for connection:
    if result.message == str("Connected !"):
        print("\nRemote device calibrated and ready for transmission !")
        update_status('Remote device calibrated and ready for transmission !')

        print("_______________________________________________________")

    else:
        # Filtering the lat-long from received message:
        result_loc = result_message.split('_')
        result_lat = float(result_loc[0][1:])
        result_long = float(result_loc[1][:-1])
        update_remote_loc(result_lat, result_long)
        update_status("Module Executing smoothly.")

        print("Received LAT : {0}".format(result_lat))
        print("Received LONG : {0}".format(result_long))
        print("MY LAT - LONG : {0} , {1}".format(self_lat, self_long))
        print("______")

        # Calculating relative co-ordinates:
        relative_lat = result_lat - self_lat
        relative_long = result_long - self_long

        print("relative lat : " + str(relative_lat))
        print("relative long : " + str(relative_long))

        latdata.append(relative_lat)
        longdata.append(relative_long)

        # Calculating distance between the two points:
        d = distance(self_lat, self_long, result_lat, result_long)

        print("Distance = {0} meters.".format(d))
        print("_______________________")
        update_distance(d)

        # Calculating points on graph based on distance:
        plot_lat = distance(self_lat, 0, result_lat, 0)
        plot_long = distance(self_long, 0, result_long, 0)

        if relative_lat < 0:
            plot_lat = 0 - plot_lat

        if relative_long < 0:
            plot_long = 0 - plot_long

        print("plot_long : " + str(plot_long))
        print("plot_lat : " + str(plot_lat))

        # Generating graph:
        ani = FuncAnimation(fig, animate(plot_lat, plot_long), frames=10, interval=200)
        plt.draw()
        plt.pause(0.1)

        # Generating output on LED Grid:
        send_to_outputter(plot_lat, plot_long)

