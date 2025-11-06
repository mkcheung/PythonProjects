from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from pathlib import Path
import requests
import smtplib

load_dotenv()
EMAIL_LOGIN_USERNAME = os.getenv('EMAIL_LOGIN_USERNAME')
EMAIL_LOGIN_PASSWORD = os.getenv('EMAIL_LOGIN_PASSWORD')
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language":"en-US"
}
priceBenchmark = 100.00
response = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
productTitle = soup.find(id='productTitle')
priceTag = soup.select("div#apex_desktop div#corePriceDisplay_desktop_feature_div span.aok-offscreen")
priceInString = priceTag[0].get_text()
priceSplit = priceInString.split("$")
price = float(priceSplit[1].strip())


if price < priceBenchmark:
    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 587) as connection:
        connection.starttls()
        connection.login(EMAIL_LOGIN_USERNAME, EMAIL_LOGIN_PASSWORD)
        template = f"""{productTitle} is now ${price}
        <a href="https://appbrewery.github.io/instant_pot/">
        https://appbrewery.github.io/instant_pot/
        </a>"""
        message = f"Subject: Price Dropped!\nContent-Type: text/html; charset=utf-8\n\n{template}"

        connection.sendmail(
            from_addr=EMAIL_LOGIN_USERNAME,
            to_addrs="test@example.com",
            msg=message.encode('utf-8')
        )

