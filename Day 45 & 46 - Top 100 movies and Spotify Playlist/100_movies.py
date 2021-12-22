from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating")
page = response.text

soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

movie_list=[]
rank_list = []
year_list = []
movies = soup.select(".lister-item-header a")
ranks = soup.find_all(class_= "lister-item-index unbold text-primary")
years = soup.find_all(class_= "lister-item-year text-muted unbold")
for tag in movies:

    movie = tag.getText()
    movie_list.append(movie)

for tag in ranks:

    rank = tag.getText()
    rank_list.append(rank)

for tag in years:

    year = tag.getText()
    year_list.append(year)

num = 0
with open("movies.txt", mode="w") as file:
    for seq in movie_list:
        text = rank_list[num] + " " + movie_list[num] + " " + year_list[num]
        num += 1
        file.write(f"{text}\n")