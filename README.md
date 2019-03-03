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
 - [Chrome WebDriver](https://chromedriver.storage.googleapis.com/index.html?path=73.0.3683.20/)
 - Python Packages :
   - [Selenium](https://www.seleniumhq.org/)
   - [PubNub Python SDK](https://www.pubnub.com/docs/python/pubnub-python-sdk)
   - [Matplotlib](https://matplotlib.org/users/installing.html)
  
 ### *Installing Chrome WebDriver :* 
 - Download the webdriver from the link above.
 - Place it in the project directory.
 - Give the path of WebDriver.exe file to the environment variables - system variable - PATH. Append the location at the end of PATH.

 
Selenium is used to access chrome - go to Google Maps - Sign In - hit the location button - zoom in - extract co-ordinates from it.

PubNub service is the online MQTT broker for handling the messages between the two devices. 
Access the [PubNub account](https://admin.pubnub.com/#/user/485567/account/485527/app/35264197/key/541883/) for authentication keys.

Matplotlib will be used to plot the real-time location of the second Raspi on the graph.

The [Haversine Formula](http://www.movable-type.co.uk/scripts/latlong.html) is used to calculate the distance between the two points in meters.
