import numpy as np
import pandas as pd
from pathlib import Path

workingDirectory = Path(__name__).resolve().parent;
# print(f"{workingDirectory}/EcommercePurchases.csv")
eCommerceDf = pd.read_csv("/Users/marscheung/SideProjects/pythonProjects/eCommerceDA/EcommercePurchases")
print(eCommerceDf.head())
#Avg Purchase Price
print(f"Average Purchase Price: ${round(eCommerceDf['Purchase Price'].mean(),2)}")

print(f"Highest Purchase Price? ${round(eCommerceDf['Purchase Price'].max(),2)}")
print(f"Lowest Purchase Price? ${round(eCommerceDf['Purchase Price'].min(),2)}")

eCommernceEngLangDf = eCommerceDf[eCommerceDf['Language'] == 'en']
print(f"Num of people with English as language of choice: {eCommernceEngLangDf['Address'].count()}")

print(f"Num purchases in AM or PM: {eCommerceDf['AM or PM'].value_counts()}")

eComAmerExp = eCommerceDf[eCommerceDf['CC Provider'] == 'American Express']
print(eComAmerExp)

eComAmerExpAbove95 = eComAmerExp[eComAmerExp['Purchase Price']>95.0]
print(f"Num People using American Express CC and have made purchase > $95.00: {eComAmerExpAbove95['Address'].count()}")

def ccExpYear(monthYear):
    dtComponent = monthYear.split("/")
    return dtComponent[1]

eCommerceDf['yearOfCCExpiration'] = eCommerceDf['CC Exp Date'].apply(ccExpYear)
print(eCommerceDf[['CC Exp Date', 'yearOfCCExpiration']])
print(f"Count of those having a Credit Card Expiring in 2025: {eCommerceDf[eCommerceDf['yearOfCCExpiration']=='25']['Address'].count()}")

def emailDomain(email):
    emailComponent = email.split("@")
    return emailComponent[1]

eCommerceDf['emailDomain'] = eCommerceDf['Email'].apply(emailDomain)
print(eCommerceDf['emailDomain'].value_counts())

print(f"Top Five Most Popular Job Titles: {eCommerceDf['Job'].value_counts()}")
print(eCommerceDf.info())

print(f"Email of CC# 4926535242672853: {eCommerceDf[eCommerceDf['Credit Card'] == 4926535242672853]['Email']}")


print(f"Purchase Price from Lot 90WT: ${round(eCommerceDf[eCommerceDf['Lot'] == '90 WT']['Purchase Price'], 2)}")

