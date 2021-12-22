from bs4 import BeautifulSoup
import requests
from datetime import date as dt

entered_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD")

current = dt.today()
current_string = current.strftime("%Y-%m-%d")

URL = "https://www.billboard.com/charts/hot-100/" + entered_date

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

rank_tag = soup.find_all(class_ ="chart-element__rank__number")
title_tag = soup.find_all(class_ ="chart-element__information__song text--truncate color--primary")
artist_tag = soup.find_all(class_ ="chart-element__information__artist text--truncate color--secondary")

# rank_list = [rank.getText() for rank in rank_tag]
title_list = [title.getText() for title in title_tag]
# artist_list = [artist.getText() for artist in artist_tag]

for num in range(len(title_list)):
    print(title_list[num])


