import datetime as dt
import pandas
from pathlib import Path
import random
import smtplib

my_email = "e6e1dacdbd3f4b"
password = "8cf8a1b6977568"

workingDirectory = Path(__file__).resolve().parent 
dataFrameBirthday = pandas.read_csv(f"{workingDirectory}/birthdays.csv")

birthdayDict = { (data_row['month'], data_row['day']): data_row for (index, data_row) in dataFrameBirthday.iterrows()}

now = dt.datetime.now()
currentDayOfWeek = now.weekday()
currentMonth = now.month
currentYear = now.year
currentMonthDay = (currentMonth, currentDayOfWeek)

if currentMonthDay in birthdayDict:
    templateNum = random.randint(1,3)
    templateAndDirectory = f"{workingDirectory}/letter_{templateNum}.txt"
    template = ''
    with open(templateAndDirectory, "r") as quoteFile:
        template = quoteFile.read()
        currentBirthday = birthdayDict[currentMonthDay]
    template = template.replace('[NAME]', currentBirthday['name'])

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@example.com",
            msg=f"Subject:Happy birthday!\n\n{template}"
        )



