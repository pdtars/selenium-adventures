from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "E:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")


def save_game():
    options = driver.find_element_by_css_selector("#prefsButton")
    options.click()
    export_save = driver.find_elements_by_css_selector("#menu .subsection .listing .option")
    export_save[1].click()

    save_game_id = driver.find_element_by_css_selector("#textareaPrompt")
    with open("save_game.txt", 'w') as file:
        file.write(save_game_id.text)

    print(f"Game Save exported successfully.\n Id: {save_game_id.text}")


for i in range(0, 15):
    cookie = driver.find_element_by_css_selector("#bigCookie")
    cookie.click()

total_cookies = driver.find_element_by_css_selector("#cookies")
print(total_cookies.text)

save_game()

# TODO Load progress
