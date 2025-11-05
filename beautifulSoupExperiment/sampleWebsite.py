from bs4 import BeautifulSoup
from pathlib import Path
# import lxml

workingDirectory = Path(__file__).resolve().parent
pathToWebsiteHtml = f"{workingDirectory}/website.html"
with open(pathToWebsiteHtml, "r") as htmlFile:
    htmlFromFile = htmlFile.read()

soup = BeautifulSoup(htmlFromFile, 'html.parser')