from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

header ={
    "Accept-Language" : "zh-CN,zh;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.65992201757813%2C%22east%22%3A-122.20673598242188%2C%22south%22%3A37.64356042534286%2C%22north%22%3A37.906788179891414%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers=header)
page = response.text

soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())

price = soup.find_all(class_= "list-card-price")
address = soup.find_all(class_= "list-card-addr")
link = soup.select(".list-card-top a")
# print(price)
price_list = []
addr_list = []
link_list = []
for tag in price:
    price_text = tag.getText()
    # try:
    if price_text.find("/") != -1:
        price_pure = price_text.split("/")[0]
    elif price_text.find("+") != -1:
        price_pure = price_text.split("+")[0]
    else:
        price_pure = price_text
    price_list.append(price_pure)

for tag in address:
    addr_text = tag.getText()
    addr_list.append(addr_text)

for tag in link:
    link_text = tag["href"]
    if link_text.find("http") == -1:
        link_pure = f"https://zillow.com{link_text}"
    else:
        link_pure = link_text
    link_list.append(link_pure)
print(price_list)
print(addr_list)
print(link_list)

CHROME_DRIVER_PATH = "/Users/aykuanwoo/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
for n in range(len(price_list)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdheb5S-8EhShEx8QnuHIJO4DWFIvXTO4SNIpG54GCWO6ITRw/viewform?usp=sf_link")
    sleep(3)
    input = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    input[0].send_keys(addr_list[n])
    input[1].send_keys(price_list[n])
    input[2].send_keys(link_list[n])
    submit = driver.find_element_by_class_name("quantumWizButtonPaperbuttonLabel")
    submit.click()

driver.quit()
