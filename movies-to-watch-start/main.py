import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movies = []
for movie in soup.find_all("h3", class_="title"):
    movies.append(movie.text)
movies.reverse()
print(movies)


with open("movies.txt", "w", encoding="utf-8") as movies_file:
    for movie in movies:
        movies_file.write(movie + "\n")

