# Necessary libraries and packages:
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
import numpy as np
import matplotlib.pyplot as plt
import geocoder

# Getting the lat-long:
g = geocoder.ip('me')
my_lat = g.latlng[0]
my_long = g.latlng[1]

# Configuring the PubNub connection:
pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-29e0c45e-724c-42ba-be7b-cb156fc74a03"
pnconfig.subscribe_key = "sub-c-f739ed7a-2afb-11e9-8c30-16f8bea0bbad"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)

# Listener to handle the subscription:
my_listener = SubscribeListener()
pubnub.add_listener(my_listener)

# Subscribing to the channel:
pubnub.subscribe().channels('ESIoT').execute()
my_listener.wait_for_connect()
print('connected')

# Making the script run continuously
while True:

    # Listening for messages:
    result = my_listener.wait_for_message_on('ESIoT')
    print(result.message)
    result_message: str = repr(result.message)

    # Filtering the lat-long from received message:
    result_loc = result_message.split('_')
    result_lat = float(result_loc[0][1:])
    result_long = float(result_loc[1][:7])
    print("Received LAT : {0}".format(result_lat))
    print("Received LONG : {0}".format(result_long))
    print("______")
    print("My Location : {0} {1}".format(my_lat, my_long))

