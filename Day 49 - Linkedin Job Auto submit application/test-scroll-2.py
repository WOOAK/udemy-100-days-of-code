from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Configure Chrome to open in fullscreen / kiosk mode.
chrome_driver_path = "/Users/aykuanwoo/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Load search results and login.
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&sortBy=R")
sign_in_button = driver.find_element_by_class_name("nav__button-secondary")
time.sleep(3)
sign_in_button.click()
time.sleep(3)
email_address = driver.find_element_by_id("username")
email_address.send_keys("aykuan1992@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Kuan1120@@")
sign_in = driver.find_element_by_class_name("login__form_action_container ")
sign_in.click()
time.sleep(3)

# Retrieve all search results and add to a list.
jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")

# For each job in the jobs list, click the Save button, scroll down to the bottom of the right hand pane and then click the Follow button.
for job in jobs:
    job.click()
    time.sleep(4)
    save_button = driver.find_element_by_class_name("jobs-save-button")
    save_button.click()
    time.sleep(2)
    # Click the right hand rail and scroll down to the bottom of the page to reveal the Follow button.
    job_detail = driver.find_element_by_class_name("jobs-search__right-rail")
    job_detail.click()
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)
    time.sleep(2)
    # Exception handling for instances in which the company does not have a Follow button.
    try:
        follow = driver.find_element_by_class_name("follow")
        follow.click()
        time.sleep(2)
    except NoSuchElementException:
        continue