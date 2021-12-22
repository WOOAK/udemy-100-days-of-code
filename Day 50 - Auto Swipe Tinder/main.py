from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "/Users/aykuanwoo/chromedriver"


driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")
time.sleep(2)

# Login at first page
login_button = driver.find_element_by_xpath('//a[@href="https://tinder.onelink.me/9K8a/3d4abb81"]')
login_button.click()
time.sleep(2)

# FB login
facebook_login = driver.find_element_by_xpath("//button[@aria-label='Login with Facebook']")
facebook_login.click()
time.sleep(2)

# Will pop to new window by FB login. Keep window handler variable. New window with n sequence +1.
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

# Must switch to new window to find elements
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(3)
email = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
email.send_keys("aykuan1992@gmail.com")
password.send_keys("kuan1120//")
password.send_keys(Keys.ENTER)

# Switch back to main page
driver.switch_to.window(base_window)
time.sleep(10)

# Dismiss requests: Allow location, disable notify, and accept cookies
allow_location = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]")
allow_location.click()
time.sleep(3)
allow_notify = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[2]")
allow_notify.click()
cookies = driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[2]/div/div/div[1]/button')
cookies.click()
time.sleep(5)
pointer = driver.find_element_by_tag_name("html")

# hitting dislike by keyboard
for n in range(10):
    pointer.send_keys(Keys.ARROW_LEFT)
    time.sleep(2)

