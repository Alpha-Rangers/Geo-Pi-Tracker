# Live-Tracker
**ESIoT Project.**

###### Track one Raspberry Pi with another one and display its trajectory as well as relative location.

### *Hardware :*
 - Raspberry Pi 3 x 2
 - Breadboard x 1
 - Wires 
 - LED x 16
 
 ### *Software :*
 - [Python 3.6](https://www.python.org/downloads/) (minimum)
 - [PyCharm IDE](https://www.jetbrains.com/pycharm/) (preferably)
 - Python Packages :
   - [Geocoder](https://geocoder.readthedocs.io/)
   - [PubNub Python SDK](https://www.pubnub.com/docs/python/pubnub-python-sdk)
   - [Matplotlib](https://matplotlib.org/users/installing.html)
  
Geocoder is used to acquire the `Latitude` and `Longititude` from the python script.

PubNub service is the online MQTT broker for handling the messages between the two devices. 
Access the [PubNub account](https://admin.pubnub.com/#/user/485567/account/485527/app/35264197/key/541883/) for authentication keys.

Matplotlib will be used to plot the real-time location of the second Raspi on the graph.
