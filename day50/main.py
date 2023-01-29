from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

import time

ser = Service("/Applications/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://tinder.com/")
# The wait is essential so the page would be fully loaded with all the elements ready
wait = WebDriverWait(driver, 20)
log_in = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Log in')))
log_in.click()

# The below while loop helped with ignoring the stale element exception until it is no longer stale
while True:
    try:
        log_in_with_facebook = wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')))
        log_in_with_facebook.click()
        break
    except StaleElementReferenceException:
        continue

tinder_window = driver.window_handles[0]
while True:
    try:
        fb_login_window = driver.window_handles[1]
        print(driver.title)
        driver.switch_to.window(fb_login_window)
        break
    except IndexError:
        continue


email = ""
password = ""
print("cookies clicked")
fb_email_form = wait.until(ec.presence_of_element_located((
    By.XPATH, '//*[@id="email"]'
)))
fb_email_form.send_keys(email)
fb_password_form = wait.until(ec.presence_of_element_located((
    By.XPATH, '//*[@id="pass"]'
)))
fb_password_form.send_keys(password)
fb_password_form.send_keys(Keys.ENTER)
driver.switch_to.window(tinder_window)
print(driver.title)

allow_location = wait.until(ec.presence_of_element_located((
    By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]'
)))
allow_location.click()

disallow_notification = wait.until(ec.presence_of_element_located((
    By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]'
)))
disallow_notification.click()
# time.sleep(60)
# cancel_mode = wait.until(ec.presence_of_element_located((
#     By.XPATH, '//*[@id="q-839802255"]/main/div/div[2]/button/svg/path'
# )))
# cancel_mode.click()
match_btn = wait.until(ec.presence_of_element_located((
        By.XPATH, '//*[@id="q888578821"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button/span/span/svg/path'
    )))
while True:
    match_btn.click()
    time.sleep(2)
driver.quit()