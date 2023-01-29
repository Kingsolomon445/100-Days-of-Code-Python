from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ser = Service("/Applications/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
total_article = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(f"{total_article.text} articles in English on Wikipedia")


# driver.get("https://www.appbrewery.co/p/newsletter")
# sign_up_form = driver.find_element(By.XPATH, '//*[@id="member_email"]')
# sign_up_form.send_keys('')
#
# submit = driver.find_element(By.XPATH, '//*[@id="profile-form-fields"]/div[1]/div/input')
# submit.click()

driver.quit()


