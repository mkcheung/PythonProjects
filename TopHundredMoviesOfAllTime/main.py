from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
best100MoviesPage = response.text
soup = BeautifulSoup(best100MoviesPage, 'html.parser')

movieTitles = soup.select("section.gallery__content-item.gallery__content-item--gallery div.article-title-description__text h3.title")
titles = [ movieTitle.get_text() for movieTitle in movieTitles ]
for title in (reversed(titles)):
    print(f"{title}")