from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/aykuanwoo/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Woo")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("AK")
email = driver.find_element_by_name("email")
email.send_keys("aykuan1992@gmail.com")
button = driver.find_element_by_css_selector("form button")
button.click()