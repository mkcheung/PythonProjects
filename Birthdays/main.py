import smtplib

my_email = "e6e1dacdbd3f4b"
password = "8cf8a1b6977568"

import datetime as dt
from pathlib import Path
import random
dt.datetime

quotes = []
workingDirectory = Path(__file__).resolve().parent
fileAndDirectory = f"{workingDirectory}/quotes.txt"

with open(fileAndDirectory, "r") as quoteFile:
    quotes = [line.strip() for line in quoteFile]

now = dt.datetime.now()
dayOfWeek = now.weekday()

if(dayOfWeek == 1):
    randomQuote = random.choice(quotes)
    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@example.com",
            msg=f"Subject:Hello\n\n{randomQuote}"
        )