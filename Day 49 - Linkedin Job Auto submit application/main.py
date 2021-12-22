from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import ElementClickInterceptedException

chrome_driver_path = "/Users/aykuanwoo/chromedriver"

# Maximize window
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# Sign in
signin_button = driver.find_element_by_link_text("Sign in")
signin_button.click()
time.sleep(3)
email = driver.find_element_by_id("username")
email.send_keys("reenie.queen.0612@gmail.com")
pw = driver.find_element_by_id("password")
pw.send_keys("Qr200612")
pw.send_keys(Keys.ENTER)

time.sleep(3)
# Prompt Not now window
try:
    not_now = driver.find_element_by_css_selector("#remember-me-prompt__form-secondary button")
    not_now.click()
except:
    pass
time.sleep(3)

# Close message chat window, in order to click "Follow Button"
message_chat = driver.find_elements_by_css_selector("button.msg-overlay-bubble-header__control")
message_chat_close = message_chat[1]
message_chat_close.click()

# Function to click job and Scroll down left pane to click for jobs which are not in view
def scroll_click(job):
    try:
        job.click()
    except ElementClickInterceptedException:
        job_summary = driver.find_element_by_class_name("jobs-search__left-rail")
        job_summary.click()
        html = driver.find_element_by_tag_name("html")
        html.send_keys(Keys.PAGE_DOWN)
        return scroll_click(job)

# All jobs listed
job_listings = driver.find_elements_by_class_name("jobs-search-results__list-item")
print(len(job_listings))
for job in job_listings:
    scroll_click(job)
    time.sleep(3)
# Scroll right pane to most bottom to get "Follow Button"
    job_detail = driver.find_element_by_class_name("jobs-search__right-rail")
    job_detail.click()
    time.sleep(3)
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)
    time.sleep(3)
    follow_button = driver.find_element_by_class_name("follow")
    follow_text = driver.find_element_by_css_selector(".follow span").text
# Avoid unfollow if the page already being followed
    if follow_text == "Follow":
        follow_button.click()

# driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element_by_css_selector("button.follow.artdeco-button.artdeco-button--secondary.ml5") )

# follow_button.click()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# try:
#     message_chat_close = driver.find_element_by_css_selector("button#ember196.msg-overlay-bubble-header__control.msg-overlay-bubble-header__control--new-convo-btn.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view")
# except:
#     message_chat_close = driver.find_element_by_css_selector("button#ember188.msg-overlay-bubble-header__control.msg-overlay-bubble-header__control--new-convo-btn.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view")
# print(message_chat_close)
# action = ActionChains(driver)
# scroll_container = driver.find_element_by_class_name("jobs-details__main-content")

# action.move_to_element(scroll_container).perform()
#driver.execute_script(f"{scroll_container}.scrollTo(0,document.body.scrollHeight)")
# driver.execute_script("window.scrollTo(0, 1080)")
# js = 'document.querySelector("button.follow.artdeco-button.artdeco-button--secondary.ml5")'
# follow_button = driver.execute_script(js)

# follow_button = driver.find_element_by_xpath('//*[@id="ember392"]/section/div[1]/div[1]/button')
# scroll_container.click()
# scroll_container.send_keys(Keys.END)

# job_listings = driver.find_elements_by_class_name("job-card-container--clickable")
    # follow_button = driver.find_element_by_css_selector(".jobs-company__box button")


