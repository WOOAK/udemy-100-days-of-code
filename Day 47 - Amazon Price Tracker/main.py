from bs4 import BeautifulSoup
import lxml
import requests
import smtplib


MY_EMAIL = "aykuan1992@gmail.com"
MY_PASSWORD = "LohZiQi0907//"
YOUR_EMAIL = "aykuan.woo@silverlakeaxis.com"
SUBJECT = "Hey, I have something to tell you!"
PRICE = 170
URL = "https://www.amazon.com/Android-10-0-Tablet-Tablets-8000mAh-Battery-WiFi/dp/B08DK1L92Y/ref=sr_1_1_sspa"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=MY_EMAIL, password=MY_PASSWORD)

header ={
    "Accept-Language" : "en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ja-JP;q=0.6,ja;q=0.5,en-US;q=0.4",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
# response = requests.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463",headers=header)
response = requests.get("https://www.amazon.com/Android-10-0-Tablet-Tablets-8000mAh-Battery-WiFi/dp/B08DK1L92Y/ref=sr_1_1_sspa",headers=header)
webpage = response.text
# print(webpage)

soup = BeautifulSoup(webpage, "lxml")
tags = soup.find(id="priceblock_ourprice")
price = float(tags.getText().split("$")[1])
tags = soup.find(id = "productTitle")
item = tags.getText().strip()
print(price)
print(item)

if price <= PRICE:
    body = f"Amazon price alert. {item} is now price {price}\n{URL}"
    message = "From: %s\r\n" % MY_EMAIL + "To: %s\r\n" % YOUR_EMAIL + "Subject: %s\r\n" % SUBJECT + "\r\n" + body
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=YOUR_EMAIL, msg=message)