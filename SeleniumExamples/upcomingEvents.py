from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opts = Options()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.python.org/")


upcomingEventsList = driver.find_element(By.CSS_SELECTOR, value="div.medium-widget.event-widget.last ul.menu")
li_elements = upcomingEventsList.find_elements(By.TAG_NAME, "li")
upcomingEvents = {}
for i, li in enumerate(li_elements):
    time = li.find_element(By.TAG_NAME, "time")
    date = time.text
    anchor = li.find_element(By.TAG_NAME, "a")
    eventName = anchor.text
    upcomingEvents[i] = {"time":date, "name":eventName}

print(upcomingEvents)
    
