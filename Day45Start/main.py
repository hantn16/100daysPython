from bs4 import BeautifulSoup
import requests as req

# with open("Day45Start/website.html", encoding="utf-8") as f:
#     content = f.read()
# bs = BeautifulSoup(content, "html.parser")
# print(bs.prettify())
# ==========================================================================
# res = req.get("https://news.ycombinator.com/news")
# yc_web_page = res.text
# soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tags = soup.find_all(name="a", class_="titlelink")
# article_texts = [x.getText() for x in article_tags]
# article_links = [x.get("href") for x in article_tags]

# article_upvotes = [int(x.getText().split(" ")[0])
#                    for x in soup.find_all(name="span", class_="score")]
# print(max(article_upvotes))
# merge_list = list(zip(article_texts, article_links, article_upvotes))
# highest_upvote_articles = [
#     x for x in merge_list if x[2] == max(article_upvotes)]
# print(highest_upvote_articles)
# ==========================================================================
res = req.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_content = res.text
soup = BeautifulSoup(web_content, "html.parser")
# movie_tags = soup.find_all(name="h3", class_="jsx-4245974604")
movie_tags = soup.select("h3.title")
list_movies_name = [x.getText().replace(":", ")") for x in movie_tags]
list_movies = sorted(list_movies_name, key=lambda x: int(x.split(r") ")[0]))
with open("./Day45Start/movies.txt", "w", encoding="utf-8") as f:
    for movie in list_movies:
        f.write(f"{movie}\n")
