from datetime import datetime
import requests
import smtplib

MY_LAT = 37.318150
MY_LONG = -121.992213

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

my_email = "e6e1dacdbd3f4b"
password = "8cf8a1b6977568"

time_now = datetime.now()
currentTimeHours = int(time_now.isoformat().split("T")[1].split(":")[0])
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

if MY_LAT >= iss_latitude-5 and MY_LAT <= iss_latitude+5 and MY_LONG >= iss_longitude-5 and MY_LONG <= iss_longitude+5 and currentTimeHours >= sunset:
    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@example.com",
            msg=f"Subject:ISS Overhead!\n\nLook up!"
        )



