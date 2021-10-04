from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "E:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)
cookie = driver.find_element_by_css_selector("#bigCookie")


######### FUNCTIONS #########
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


def get_market_items():
    store_item = driver.find_elements_by_css_selector("#store #products .product.unlocked.enabled")  # .title")
    store_item_price = driver.find_elements_by_css_selector("#store #products .product.unlocked.enabled .price")

    item_ids = [item.get_attribute("id") for item in store_item]
    item_prices = [int(item.text) for item in store_item_price]

    item_and_prices = {item_ids[item]: item_prices[item] for item in range(len(item_ids))}

    return item_and_prices


######### END FUNCTIONS #########

# load_game("save_game.txt")

baking_timer = time.time() + 300
time_break = time.time() + 5

while baking_timer > time.time():
    cookie.click()

    # Get item prices
    if time.time() >= time_break:
        item_and_prices = get_market_items()
        if len(item_and_prices) == 0:
            continue
        # print(item_and_prices)

    # Get cookie count(i.e. money) for store purchases
        _ = driver.find_element_by_css_selector("#cookies")
        cookie_text_string = _.text
        cookie_text_string = cookie_text_string.split()
        #CPS = int(cookie_text_string[-1])
        total_cookies = int(cookie_text_string[0])

        #Buy upgrades
        for k, v in item_and_prices.items():
            while True:
                if total_cookies >= item_and_prices[k]:
                    prod = driver.find_element_by_id(k)
                    prod.click()
                    total_cookies -= item_and_prices[k]
                    time.sleep(1)
                else:
                    break

        time_break = time.time() + 5



#TODO Implementar compra de upgrades dos items da store

time.sleep(2)
# save_game()
