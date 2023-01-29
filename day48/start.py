from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("/Applications/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://www.python.org/")
upcoming_events = driver.find_elements(By.CSS_SELECTOR, '#content > div > section > div.list-widgets.row > '
                                                        'div.medium-widget.event-widget.last > div > ul > li > a')
events_date = driver.find_elements(By.CSS_SELECTOR, '#content > div > section > div.list-widgets.row > '
                                                    'div.medium-widget.event-widget.last > div > ul > li > time')
events = {idx: {'name': upcoming_events[idx].text, 'date': events_date[idx].text} for idx in range(len(events_date))}
print(events)
driver.quit()
