from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys

ser = Service("/Applications/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookieclicker = driver.find_element(By.XPATH, '//*[@id="cookie"]')
timeout = time.time() + 60*5
time_after_5sec = time.time() + 5
while True:
    if time.time() > time_after_5sec:
        money = driver.find_element(By.XPATH, '//*[@id="money"]').text
        money = money.replace(',', '')
        money = int(money)
        if money > 7000:
            buy_addon = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
        elif money > 2000:
            buy_addon = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
        elif money > 500:
            buy_addon = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
        elif money > 100:
            buy_addon = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
        buy_addon.click()
        time_after_5sec = time.time() + 5
    cookieclicker.click()
    if time.time() > timeout:
        break

my_rate = driver.find_element(By.XPATH, '//*[@id="cps"]').text
print(f"My rate of playing , {my_rate}")
driver.quit()
