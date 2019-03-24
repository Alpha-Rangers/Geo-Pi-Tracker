# Necessary libraries and packages:
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Using Selenium to access Chrome:
chrome_options = Options()
driver = webdriver.Chrome()
driver.set_window_size(500, 500)

# Opening Google maps:
driver.get("https://google.co.in/maps")

# Signing in:
while True:
    try:
        sign_in = driver.find_element_by_id('gb_70')
        break
    except Exception:
        time.sleep(0.1)
        continue
sign_in.click()

# Entering credentials:
while True:
    try:
        username = driver.find_element_by_id('identifierId')
        username.send_keys("sudhanshu1k")

        next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
        break

    except Exception:
        time.sleep(0.1)
        continue

next_button.click()


# Entering Password:
while True:
    try:
        password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password.send_keys("krinkhold13", Keys.ENTER)
        break

    except Exception:
        time.sleep(0.1)
        continue

# Getting the location:
while True:
    try:
        location_button = driver.find_element_by_xpath('//*[@id="widget-mylocation"]')
        break
    except Exception:
        time.sleep(0.1)
        continue
location_button.click()

# Zooming in:
while True:
    try:
        zoom_button = driver.find_element_by_xpath('//*[@id="widget-zoom-in"]')
        break
    except Exception:
        time.sleep(0.1)
        continue

for i in range(5):
        zoom_button.click()
        time.sleep(2)

print(driver.current_url)

# Getting info:
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

envelope = pubnub.publish().channel("ESIoT").message("Connected !").sync()

# Making the script run continuously:
while True:

    # Getting the location:
    location_button = driver.find_element_by_xpath('//*[@id="widget-mylocation"]')
    location_button.click()
    while True:
        try:
            zoom_button = driver.find_element_by_xpath('//*[@id="widget-zoom-in"]')
            break
        except Exception:
            time.sleep(0.1)
            continue

    for i in range(5):
        zoom_button.click()
        time.sleep(2)

    # Getting info:
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

    # Setting time interval to 5 sec:
    time.sleep(5)


