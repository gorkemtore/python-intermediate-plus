from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.a.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

top_index = article_upvotes.index(max(article_upvotes))

print(f"{article_texts[top_index]} \n{article_links[top_index]} \n{article_upvotes[top_index]}")