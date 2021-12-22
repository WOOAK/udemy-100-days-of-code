from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = "/Users/aykuanwoo/chromedriver"
IG_EMAIL = "reenie.queen.handcrafts"
IG_PASSWORD = "Qr200612"
SIMILAR_ACCOUNT = "treasure.boxmy"


class InstaFollower:
    def __init__(self, path):
        super().__init__()
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get(f"https://www.instagram.com/")
        sleep(5)
        username = self.driver.find_element_by_name("username")
        username.send_keys(IG_EMAIL)
        password = self.driver.find_element_by_name("password")
        password.send_keys(IG_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)
    def find_followers(self):
        search_button = self.driver.find_element_by_xpath(("//input[@type='text']"))
        search_button.send_keys(SIMILAR_ACCOUNT)
        sleep(5)
        search_button.send_keys(Keys.ARROW_DOWN)
        search_button.send_keys(Keys.ENTER)
        sleep(5)
        follower_button = self.driver.find_element_by_xpath('//a[@href="/treasure.boxmy/followers/"]')
        follower_button.click()

    def follow(self):

        for n in range(50):
            follower_list = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
            follower_list.click()
            html = self.driver.find_element_by_tag_name("html")
            html.send_keys(Keys.PAGE_DOWN)
            sleep(3)

        all_buttons = self.driver.find_elements_by_css_selector("li button")
        print(all_buttons)
        for button in all_buttons:
            if button.text == "Follow":
                button.click()
                sleep(1)
                print("Hey")
        # # html = self.driver.find_element_by_tag_name("html")
        # html.send_keys(Keys.PAGE_DOWN)

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()


