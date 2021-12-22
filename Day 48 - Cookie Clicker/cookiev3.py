from selenium import webdriver
import time

chrome_driver_path = "/Users/aykuanwoo/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id('cookie')

tt_end = time.time() + 300
while time.time() < tt_end:  # 5 minute outer loop
    t_end = time.time() + 5
    while time.time() < t_end:  # 5 second inner loop
        cookie.click()
    store_items = driver.find_elements_by_css_selector('#store div')
    for n in range(len(store_items) - 1, 0, -1):  # iterate from most expensive items
        try:
            store_items[n].get_attribute('onclick')  # test for click
            store_items[n].click()

        except:
            pass

cps = driver.find_element_by_css_selector('#cps')
print(cps.text)

driver.close()