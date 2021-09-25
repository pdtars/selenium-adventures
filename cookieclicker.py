from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "E:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

#url = driver.command_executor._url #http://127.0.0.1:62555
#session_id = driver.session_id #824a355500ca27a95801bed9ecbcd79d

for i in range(0, 1000):
    cookie = driver.find_element_by_css_selector("#bigCookie")
    cookie.click()


total_cookies = driver.find_element_by_css_selector("#cookies")
print(total_cookies.text)

#save = driver.find_element_by_css_selector()

# TODO Save progress

# TODO Load progress





