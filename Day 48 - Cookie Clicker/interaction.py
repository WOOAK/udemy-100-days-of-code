from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/Users/aykuanwoo/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# link = driver.find_element_by_css_selector("#articlecount a")
# link.click()
# portal_link = driver.find_element_by_link_text("All portals")
# portal_link.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

