from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/aykuanwoo/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://stackoverflow.com/questions/41758095/python-selenium-scrolling-not-working/41758376")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
