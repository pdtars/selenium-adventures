from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "E:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)


def save_game():
    time.sleep(1)
    options = driver.find_element_by_css_selector("#prefsButton")
    options.click()
    time.sleep(1)

    export_save = driver.find_elements_by_css_selector("#menu .subsection .listing .option")
    export_save[1].click()

    save_game_id = driver.find_element_by_css_selector("#textareaPrompt")
    with open("save_game.txt", 'w') as file:
        file.write(save_game_id.text)

    print(f"Game Save exported successfully.\n Id: {save_game_id.text}")


def load_game(save_file):
    with open(save_file) as file:
        save = file.readline()
    print(save)

    options = driver.find_element_by_css_selector("#prefsButton")
    options.click()

    import_save = driver.find_elements_by_css_selector("#menu .subsection .listing .option")
    import_save[2].click()

    paste_save = driver.find_element_by_css_selector("#textareaPrompt")
    paste_save.send_keys(save)
    time.sleep(3.0)

    click_load = driver.find_element_by_xpath('//*[@id="promptOption0"]')
    click_load.click()
    time.sleep(1.0)

    close_option_menu = driver.find_element_by_xpath('//*[@id="menu"]/div[1]')
    close_option_menu.click()


load_game("save_game.txt")

for i in range(0, 10):
    cookie = driver.find_element_by_css_selector("#bigCookie")
    cookie.click()

total_cookies = driver.find_element_by_css_selector("#cookies")
print(total_cookies.text)

time.sleep(2)
save_game()
