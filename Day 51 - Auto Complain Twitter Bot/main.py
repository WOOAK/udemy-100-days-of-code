from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 35
PROMISED_UP = 12
CHROME_DRIVER_PATH = "/Users/aykuanwoo/chromedriver"
TWITTER_EMAIL = "aykuan1992@gmail.com"
TWITTER_PASSWORD = "Kuan1120@@"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        super().__init__()
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(5)
        go_button = self.driver.find_element_by_class_name("js-start-test")
        go_button.click()
        sleep(40)
        down = self.driver.find_element_by_css_selector("span.download-speed")
        up = self.driver.find_element_by_css_selector("span.upload-speed")
        return float(down.text), float(up.text)

    def tweet_at_provider(self, msg):
        self.driver.get("https://twitter.com/")
        sleep(5)
        login_button = self.driver.find_element_by_xpath('//a[@href="/login"]')
        login_button.click()
        sleep(5)
        username = self.driver.find_element_by_name("session[username_or_email]")
        password = self.driver.find_element_by_name("session[password]")
        username.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)

        tweet_content = self.driver.find_element_by_class_name("public-DraftStyleDefault-block")
        tweet_content.send_keys(msg)
        tweet_post = self.driver.find_element_by_xpath("//div[@data-testid='tweetButtonInline']")
        tweet_post.click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
actual_down, actual_up = bot.get_internet_speed()
print(actual_down)
print(actual_up)
if actual_down < PROMISED_DOWN or actual_up < PROMISED_UP:
    message = f"Hey Unifi Malaysia, why is my internet speed {actual_down}down/{actual_up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
    bot.tweet_at_provider(message)

