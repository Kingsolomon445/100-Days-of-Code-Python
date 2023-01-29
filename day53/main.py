# https://docs.google.com/forms/d/e/1FAIpQLSeCQLvzjyBYDbjKdxbFxIZCvVapR-p8QMmhBUoRDu25ob3utw/viewform?usp=sf_link
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

import requests

city = input("What city(If your city has more than one words, separate with an hyphen(-))?  ").title()
state = input("What state(Write only the two letters initial e.g ca for california?  ").upper()
address = f"https://www.realtor.com/apartments/{city}_{state}"
response = requests.get(address)
#response.raise_for_status()
print(response.text)
with open("file.txt", 'w') as file:
    file.write(response.text)


ser = Service("/Applications/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.implicitly_wait(30)
driver.maximize_window()

driver.get(address)
#zpid_2060673762 > div > div.StyledPropertyCardDataWrapper-c11n-8-73-8__sc-1omp4c3-0.gXNuqr.property-card-data > div.StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0.hRqIYX
# response = requests.get(address)
# response.raise_for_status()
# contents = response.text
#
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup)