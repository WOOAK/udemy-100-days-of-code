from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path =                    
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

def check_price(wang):
    global id_string
    buy_str = "buy"
    item_list = ["Cursor", "Grandma", "Factory", "Mine", "Shipment", "Alchemy lab", "Portal", "Time machine"]
    for n in range(len(item_list)):
        id_string = buy_str + item_list[n]
        price = driver.find_element_by_id(f"{id_string}").text.split("-")[1].split()[0]
        if "," in price:
            price = price.replace(",","")

        if int(price)>= wang:
            break
    if n!=0:
        id_string = buy_str + item_list[n - 1]
    buy_item = driver.find_element_by_id(id_string)
    buy_item.click()


start_time = time.time()
timeout = start_time + 60 * 5
print(start_time)
print(timeout)

while time.time() < timeout:
    cookie.click()
    if time.time() - start_time >= 5:
        print(time.time())
        print(start_time)
        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(",", "")
        check_price(int(money))
        start_time = time.time()
cps = driver.find_element_by_id("cps").text
print(cps)
# n = 1
# while n <= 7020:
#     cookie.click()
#     n += 1







# amount_info = amount_elem.text.split("-")
# amount = amount_info[1].strip()
