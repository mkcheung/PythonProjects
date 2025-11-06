from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opts = Options()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://secure-retreat-92358.herokuapp.com/")


firstNameInput = driver.find_element(By.NAME, value="fName")
lastNameInput = driver.find_element(By.NAME, value="lName")
emailInput = driver.find_element(By.NAME, value="email")
signupButton = driver.find_element(By.TAG_NAME, 'button')

firstNameInput.send_keys('Mars')
lastNameInput.send_keys('Cheung')
emailInput.send_keys('mars.kwong.cheung@gmail.com')
signupButton.click()
    


