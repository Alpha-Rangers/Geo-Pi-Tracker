# Necessary libraries and packages:
import geocoder
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time

# Configuring the PubNub connection:
pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-29e0c45e-724c-42ba-be7b-cb156fc74a03"
pnconfig.subscribe_key = "sub-c-f739ed7a-2afb-11e9-8c30-16f8bea0bbad"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)

# Assigning IP to Geocoder for tracking the location:
g = geocoder.ip('me')

# Making the script run continuously
while True:

    # Getting the lat-long:
    locData = repr(g.latlng[0]) + '_' + repr(g.latlng[1])

    print(locData)

    # Publishing to the PubNub Service:
    envelope = pubnub.publish().channel("ESIoT").message(locData).sync()
    print("publish timetoken: {0}".format(envelope.result.timetoken))

    print("Sent !")
    print("______")

    # Setting time interval to 1 sec.
    time.sleep(1)

