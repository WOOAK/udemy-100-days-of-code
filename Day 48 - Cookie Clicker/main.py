from selenium import webdriver
chrome_driver_path = "/Users/aykuanwoo/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/Seagate-Portable-External-Hard-Drive/dp/B07CRG7BBH/ref=sr_1_2?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=8YSAAAB9H67SVR11G8W0&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1624659312&rnid=16225007011&s=computers-intl-ship&sr=1-2&th=1")
driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)
search_bar = driver.find_element_by_name("q")

# Get HTML tag name
print(search_bar.tag_name)
print(search_bar.get_attribute('placeholder'))
logo = driver.find_element_by_class_name("python-logo")
print(logo.size)

# for tag which dont have specific class name, id name, select class that higher hierarchy
documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

# for tag which still hard to be found by using selector, use xpath: inspect> select > copy > copy xpath
bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# notes
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a
# {key: {key:value},key: {key:value}}

# my xpath solution: cons - u need to know number of rows of events
# event_dict = {}
# for n in range(1,6,1):
#     # print(n)
#     event_time= driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{n}]/time')
#     # print(event_time.text)
#     event_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{n}]/a')
#     # print(event_name.text)
#     seq = n-1
#     event_dict[seq] = {
#         "time":event_time.text, "name":event_name.text
#     }

# angela's css selector solution. pros: no need to know number of row of event
event_dict = {}
event_time = driver.find_elements_by_css_selector(".event-widget time")
event_name = driver.find_elements_by_css_selector(".event-widget li a")
for n in range(len(event_time)):
    event_dict[n] = {
        "time":event_time[n].text, "name":event_name[n].text
    }
print(event_dict)


driver.close()
# driver.quit()