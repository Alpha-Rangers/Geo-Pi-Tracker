# Necessary libraries and packages:
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Using Selenium to access Chrome
chrome_options = Options()
driver = webdriver.Chrome()
driver.set_window_size(500, 500)

# Opening Google maps
driver.get("https://google.co.in/maps")
time.sleep(15)

# Signing in
sign_in = driver.find_element_by_id('gb_70')
sign_in.click()
time.sleep(10)

username = driver.find_element_by_id('identifierId')
username.send_keys("sudhanshu1k")
next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
next_button.click()
time.sleep(2)

password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys("krinkhold13")
after_pass = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
after_pass.click()
time.sleep(10)

# Getting the location
location_button = driver.find_element_by_xpath('//*[@id="widget-mylocation"]')
location_button.click()

# Zooming in
time.sleep(5)
zoom_button = driver.find_element_by_xpath('//*[@id="widget-zoom-in"]')

for i in range(5):
        zoom_button.click()
        time.sleep(2)

print(driver.current_url)

# Getting info
url_strings = repr(driver.current_url).split("@")
url_location = url_strings[1].split(",")
url_lat = url_location[0]
url_long = url_location[1]
print("LAT : {0}".format(url_lat))
print("LONG : {0}".format(url_long))
locData = url_lat + '_' + url_long

# Configuring the PubNub connection:
pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-29e0c45e-724c-42ba-be7b-cb156fc74a03"
pnconfig.subscribe_key = "sub-c-f739ed7a-2afb-11e9-8c30-16f8bea0bbad"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)

# Making the script run continuously
while True:

    # Getting the location
    location_button = driver.find_element_by_xpath('//*[@id="widget-mylocation"]')
    location_button.click()

    url_strings = repr(driver.current_url).split("@")
    url_location = url_strings[1].split(",")
    url_lat = url_location[0]
    url_long = url_location[1]
    locData = url_lat + '_' + url_long

    # Publishing to the PubNub Service:
    envelope = pubnub.publish().channel("ESIoT").message(locData).sync()
    print("publish timetoken: {0}".format(envelope.result.timetoken))

    print("Sent : {0}".format(locData))
    print("______")

    # Setting time interval to 1 sec.
    time.sleep(1)


