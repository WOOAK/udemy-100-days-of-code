from selenium import webdriver
from threading import Timer

END_TIME = 300  # 5min*60s = 300s
PURCHASE_TIME = 1

# Using Windows
chrome_driver_path = "/Users/aykuanwoo/chromedriver"

game_on = True


def purchase_phase():
    global game_on

    # purchase_phase to be called every 1 second(s)
    t = Timer(PURCHASE_TIME, purchase_phase)
    t.start()

    if not game_on:
        t.cancel()
        return

    # ------ BUY COOKIE MAKERS --------------------------------------------------

    # Find the highest level of Cookie Makers Available/Unlocked
    cookie_maker = driver.find_elements_by_css_selector("#store #products .unlocked")
    cookie_maker_lvl = len(cookie_maker) - 1  # Minus 1 to fix index offset

    try:
        # Check how many Cookie Makers you have of the second highest level available/unlocked (highest level not optimal)
        qty = driver.find_elements_by_css_selector("#store #products .unlocked .owned")
        qty = int(qty[cookie_maker_lvl - 1].get_attribute("textContent"))

        # Don't by next level until 8 of the current level Cookie Makers are purchased (starting with Grandmas)
        if qty < 8 and cookie_maker_lvl > 1:
            try:
                cookie_maker[cookie_maker_lvl - 1].click()
            except IndexError:
                pass
    except:
        pass

    # Buy the next level of Cookie Makers available (after maxing out 8 of the previous level)
    try:
        cookie_maker[cookie_maker_lvl].click()
    except IndexError:
        pass

    # ------ Upgrades -----------------------------------------------------------
    try:
        crate_upgrade = driver.find_element_by_css_selector("#store .crate")
        crate_upgrade.click()
    except:
        pass

    # ------ Reindeer check/click -----------------------------------------------
    try:
        reindeer = driver.find_element_by_css_selector(".shimmer")
        reindeer.click()
    except:
        pass


def close_game():
    global game_on
    game_on = False
    score = driver.find_elements_by_css_selector("#game #cookies")
    print(score[0].text.split()[5])
    driver.close()


# === PROGRAM START =============================================================

# Initiate Selenium
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Create element for the big cookie
cookie = driver.find_element_by_id("bigCookie")

# Set Timer for end of game
t2 = Timer(END_TIME, close_game)
t2.start()

# Check what can be purchased and purchase it (Function will loop by calling itself)
purchase_phase()

# Click the Big Cookie forever until the game closes
while game_on:
    cookie.click()