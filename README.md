# Geo-Pi Tracker
**ESIoT Project.**

###### Track one Raspberry Pi with another one and display its trajectory as well as relative location.

### *Hardware :*
 - Raspberry Pi 3 x 2
 - Breadboard x 1
 - IC 7404 (NOT Gate) x 1
 - IC 74138 (1:8 DeMUX) x 2
 - Single layer PCB
 - LED x 16
 - Android devices x 2
 
 ### *Software :*
 - [Python 3.6](https://www.python.org/downloads/) (minimum)
 - [PyCharm IDE](https://www.jetbrains.com/pycharm/) (preferably)
 - [Chrome WebDriver](https://chromedriver.storage.googleapis.com/index.html?path=73.0.3683.20/)
 - [Pydroid](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=en_IN)
 - Python Packages :
   - [Selenium](https://www.seleniumhq.org/)
   - [PubNub Python SDK](https://www.pubnub.com/docs/python/pubnub-python-sdk)
   - [Matplotlib](https://matplotlib.org/users/installing.html)
   - [Plyer](https://pypi.org/project/plyer/)
  
 ### *Installing Chrome WebDriver :* 
 - Download the webdriver from the link above.
 - Place it in the project directory.
 - Give the path of WebDriver.exe file to the environment variables - system variable - PATH. Append the location at the end of PATH.

 #### *Using Pydroid :*
 - Download Pydroid from the link above, on your Android Device.
 - Download an additional [plugin](https://play.google.com/store/apps/details?id=ru.iiec.pydroidpermissionsplugin&hl=en) which will grant permissions to Pydroid for accessing device's GPS module.
 - Once both are installed, install proper libraries in Pydroid using Pip integration found in the sidebar.
 - Open a new file and copy the appropriate script and execute.

Selenium is used for web browser automation. To access chrome - go to Google Maps - Sign In - hit the location button - zoom in - extract co-ordinates from it.

PubNub service is the online MQTT broker for handling the messages between the two devices. 
Access the [PubNub account](https://admin.pubnub.com/#/user/485567/account/485527/app/35264197/key/541883/) for authentication keys.

Matplotlib will be used to plot the real-time location of the second Raspi on the graph.

Pydroid is used to run Python scripts on Android, which will use the device's gps location and transmitt it back to Raspberry Pis

The [Haversine Formula](http://www.movable-type.co.uk/scripts/latlong.html) is used to calculate the distance between the two points in meters.


[Find more details about the project.](https://docs.google.com/document/d/1KCYRFPLAYCFK_cW10q42ZrTNj4GCa3kxpJBWMFR7w-s/edit?usp=sharing)
