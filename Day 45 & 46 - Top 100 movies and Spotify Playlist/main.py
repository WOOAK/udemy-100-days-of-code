from bs4 import BeautifulSoup
import lxml
import requests

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(contents)

# HTML tag name
# print(soup.title.name)
#
# # String contained in HTML tag
# print(soup.title.string)
# print(soup)
#
# # proper indent
# print(soup.prettify())

# # first anchor tag
# print(soup.a)
# # first li tag
# print(soup.li)

# list of HTML codes with anchor tag
# all_anchors = soup.find_all(name="a")

# get string of HTML tag
# for tag in all_anchors:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id = "name")
#
# print(heading)
#
# subheading = soup.find(name="h3", class_ = "heading")
# print(subheading)
# print(subheading.get("class"))
#
# # select first HTML which is in p and a tag
# company_link = soup.select_one(selector="p a")
# name = soup.select_one(selector="#name")
#
# print(company_link)
# print(name)
#
# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

news_titles = []
news_links = []
news_tag = soup.find_all(name = "a", class_ = "storylink")
print(news_tag)

for tag in news_tag:
    news_title = tag.string
    news_titles.append(news_title)
    news_link = tag.get("href")
    news_links.append(news_link)


# news_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
news_upvotes = []
subtexts = soup.find_all(name="td", class_="subtext")
for subtext in subtexts:
    if not subtext.find(name="span", class_="score"):
        news_upvotes.append(0)
    else:
        news_upvotes.append(int(subtext.find(name="span", class_="score").getText().split()[0]))

highest = max(news_upvotes)
highest_index = news_upvotes.index(highest)


print(news_titles[highest_index])
print(news_links[highest_index])
print(highest)




