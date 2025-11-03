from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import requests
import smtplib

my_email = "e6e1dacdbd3f4b"
password = "8cf8a1b6977568"
lat = 37.318150
long = -121.992210
api_key = "914115924065279f1fe4ee04242bafb6"
api = "https://api.openweathermap.org/data/2.5/forecast"
weatherparams = {
    "lat": lat,
    "lon": long,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=api, params=weatherparams)
weather_data = response.json()
for weather in weather_data['list']:
    # datetime_object_local = datetime.fromtimestamp(weather['dt'])
    utc_dt = datetime.fromtimestamp(weather['dt'], tz=ZoneInfo("UTC"))
    pst_dt = utc_dt.astimezone(ZoneInfo("America/Los_Angeles"))
    if weather['weather'][0]['id'] < 700:
        with smtplib.SMTP("sandbox.smtp.mailtrap.io", 587) as connection:
            rainWarningMsg = f"Date:{pst_dt} - Condition Codes: {weather['weather'][0]['id']} - Bring an umbrella."
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="test@example.com",
                msg=f"Subject:Rain!\n\n{rainWarningMsg}"
            )
