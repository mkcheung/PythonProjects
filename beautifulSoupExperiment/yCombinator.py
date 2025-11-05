from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
# target_trs = soup.find_all("tr", class_="athing submission") 
# article_texts = []
# article_links = []
# for tr in target_trs:
#     articles = tr.find_all("span", class_="titleline")
#     for anchor in articles:
#         article_tag = anchor.find("a")
#         text = article_tag.getText()
#         article_texts.append(text)
#         link = article_tag.get("href")
#         article_links.append(link)    

article_tags = soup.select("tr.athing.submission span.titleline a")
article_texts = [a.get_text() for a in article_tags]
article_links = [a["href"]for a in article_tags]

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)