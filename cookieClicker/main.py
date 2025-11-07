from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, time

opts = Options()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)
englishLangButton = driver.find_element(By.ID, 'langSelect-EN')
if englishLangButton: 
    englishLangButton.click()

sleep(2)
five_seconds_passed = time() + 5  # five second passed current time
five_min_interval = time() + 60 * 5  # Run for 5 minutes
cookie = driver.find_element(By.ID, 'bigCookie')
gameRunning = True;
timeAtBegin = time();
while gameRunning:
    cookie.click()

    if time() > five_seconds_passed:
        itemsAndPrices = {}
        items = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")       
        for item in items:
            if "enabled" in item.get_attribute("class"):
                itemId = item.get_attribute('id')
                itemPriceText = item.find_element(By.CLASS_NAME, "price")
                itemsAndPrices[itemId]=float(itemPriceText.text.replace(",", "").strip())
        
        if len(itemsAndPrices) > 0:
            productIdOfMostExpensive = max(itemsAndPrices, key=itemsAndPrices.get)
            productToPurchase = driver.find_element(By.ID, productIdOfMostExpensive)
            productToPurchase.click()

        five_seconds_passed = time() + 5 

    if time() > five_min_interval:
        cookieCounter = driver.find_elements(By.ID, 'cookies')      
        cookieCounterText = cookieCounter[0].text  
        cctSplit = cookieCounterText.split()
        timeAtEnd = time()
        secondsElapsed = timeAtEnd - timeAtBegin
        numCookies = int(cctSplit[0])
        cookiesToSecond = round(float(numCookies/secondsElapsed),2)
        print(f"cookies/second : {str(cookiesToSecond)}")
        gameRunning = False