from datetime import date, timedelta
import requests
import smtplib

my_email = "e6e1dacdbd3f4b"
password = "8cf8a1b6977568"

alphavantageapikey = "FDPSS283D24YAT6I"
newsapiapiKey = "54ff1ae952d4410e9dda1378bd306513"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

aVParameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": alphavantageapikey,
}

newsApiParameters = {
    "apiKey": newsapiapiKey,
    "q": "Tesla",
    "sortBy": "popularity",
}

response = requests.get(url=STOCK_ENDPOINT, params=aVParameters)
response.raise_for_status()
pastStockPriceData = response.json()
yesterdayClosingPrices = { key:value['4. close'] for (key, value) in pastStockPriceData['Time Series (Daily)'].items()}

today = date.today()
yesterday = today - timedelta(days=3);
yesterdayString = f"{yesterday.year}-{f"0{yesterday.month}" if yesterday.month < 10 else f"{yesterday.month}"}-{f"0{yesterday.day}" if yesterday.day < 10 else f"{yesterday.day}"}"
try:
    yesterdayClosingPrice = round(float(yesterdayClosingPrices[yesterdayString]),2)
    print(f"Closing Stock Price on {yesterdayString}: ${yesterdayClosingPrice}")
except:
    print(f"No closing stock price on {yesterdayString}.")

dayBeforeYesterday = today - timedelta(days=4)
dbyString = f"{dayBeforeYesterday.year}-{f"0{dayBeforeYesterday.month}" if dayBeforeYesterday.month < 10 else str(dayBeforeYesterday.month)}-{f"0{dayBeforeYesterday.day}" if dayBeforeYesterday.day < 10 else str(dayBeforeYesterday.day)}"
try:
    dayBeforeYesterdayClosingStockPrice = round(float(yesterdayClosingPrices[dbyString]),2)
    print(f"Closing Stock Price on {dbyString}: ${dayBeforeYesterdayClosingStockPrice}")
except:
    print(f"No closing stock price on {dbyString}.")

absDifference = abs(dayBeforeYesterdayClosingStockPrice - yesterdayClosingPrice)

percentDifference = abs(round(((dayBeforeYesterdayClosingStockPrice - yesterdayClosingPrice) / yesterdayClosingPrice) * 100, 2));
print(f"{percentDifference}% change")
response = requests.get(url=NEWS_ENDPOINT, params=newsApiParameters)
response.raise_for_status()
pastArticleResponse = response.json()
articles = pastArticleResponse['articles']
titleAndLinks = [ value['url'] for (value) in articles ]

threeMostPopularArticles = titleAndLinks[:3]
articlesForUser = f"\n".join(threeMostPopularArticles)
with smtplib.SMTP("sandbox.smtp.mailtrap.io", 587) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="test@example.com",
        msg=f"Subject:Popular Tesla Articles!\n\n{articlesForUser}"
    )


