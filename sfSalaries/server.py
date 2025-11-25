import numpy as np
import pandas as pd
from pathlib import Path

workingDirectory = Path(__name__).resolve().parent;
sfSalariesDf = pd.read_csv('Salaries.csv')

print(sfSalariesDf.head())
avgBasePay = round(sfSalariesDf['BasePay'].mean(),2)
print(f"Average Base Pay: ${avgBasePay}")

highestOvertimePayAmt = sfSalariesDf['OvertimePay'].max()
print(f"Highest Amt of Overtime Pay: ${highestOvertimePayAmt}")

jDriscollJobTitle = sfSalariesDf[sfSalariesDf['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
jDriscollTotalPayBenefits = sfSalariesDf[sfSalariesDf['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
print(f"John Driscoll Job Title: {jDriscollJobTitle} | Rate of Pay: {jDriscollTotalPayBenefits} ")

highestTotPay = sfSalariesDf['TotalPayBenefits'].max()
highestPayPerson = sfSalariesDf[sfSalariesDf['TotalPayBenefits']==highestTotPay]['EmployeeName']
print(f"Highest Paid Person: {highestPayPerson}")

lowestTotPay = sfSalariesDf['TotalPayBenefits'].min()
lowestPayPerson = sfSalariesDf[sfSalariesDf['TotalPayBenefits']==lowestTotPay]['EmployeeName']
print(f"Lowest Paid Person: {lowestPayPerson}")

sfSDMeanOfPayByYear = round(sfSalariesDf.groupby('Year')['BasePay'].mean(),2)
print(f"Mean BasePay of all employees per year: ${sfSDMeanOfPayByYear}")

print(f"Number of Distinct Jobs: {sfSalariesDf['JobTitle'].nunique()}")

numOccurJobs = sfSalariesDf.groupby('JobTitle').size().sort_values(ascending=False)
print(numOccurJobs)

top5MostCommonJobs = sfSalariesDf['JobTitle'].value_counts().head(5)
print(f"Top 5 Most Common Jobs: {top5MostCommonJobs}")



# Number Of Jobs held by only one person in 2013
sfSalaries2013 = sfSalariesDf[sfSalariesDf['Year'] == 2013][['JobTitle','EmployeeName']].groupby('JobTitle').agg({'EmployeeName':'count'}).sort_values('EmployeeName')
print(f"Number of Job Titles with ONLY one person in 2013? {sfSalaries2013[sfSalaries2013['EmployeeName']==1]['EmployeeName'].sum()}")


def isChiefInTitle(title):
    chiefSubStrUpper = 'CHIEF'
    return 1 if chiefSubStrUpper in title else 0

sfSalariesDf['hasChief'] = sfSalariesDf['JobTitle'].apply(isChiefInTitle)
print(f"Number of Job Titles with 'Chief': {sfSalariesDf['hasChief'].sum()}")

