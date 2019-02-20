import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome()

driver.get("https://google.co.in/maps")
time.sleep(7)

sign_in = driver.find_element_by_id('gb_70')
sign_in.click();
time.sleep(10)

username = driver.find_element_by_id('identifierId')
username.send_keys("shubhamverma3542")
next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
next_button.click()
time.sleep(2)

password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys("vasushena")
after_pass = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
after_pass.click()
time.sleep(10)

location_button = driver.find_element_by_xpath('//*[@id="widget-mylocation"]')
location_button.click()

time.sleep(5)
zoom_button = driver.find_element_by_xpath('//*[@id="widget-zoom-in"]')

for i in range(5):
        zoom_button.click()
        time.sleep(2)

print(driver.current_url)

url_strings = repr(driver.current_url).split("@")
url_location = url_strings[1].split(",")
url_lat = url_location[0]
url_long = url_location[1]
print("LAT : {0}".format(url_lat))
print("LONG : {0}".format(url_long))