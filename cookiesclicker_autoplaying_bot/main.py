import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "C:\Development\chromedriver"
TIME_DELTA = 1 * 60


def main():
    service = Service(chrome_driver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Users\Admin\AppData\Local\CocCoc\Browser\Application\browser.exe"
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
    driver.get("http://orteil.dashnet.org/experiments/cookie/")
    cookie = driver.find_element(by=By.ID, value="cookie")
    list_item = driver.find_elements(
        by=By.CSS_SELECTOR, value="div#store>div")
    item_ids = [item.get_attribute("id") for item in list_item]
    time_end = time.time() + TIME_DELTA
    time_out = time.time()+5
    while time.time() < time_end:
        cookie.click()
        if time.time() > time_out:
            # Get all upgrade <b> tags
            all_prices = driver.find_elements_by_css_selector("#store b")
            item_prices = []

            # Convert <b> text into an integer price.
            for price in all_prices:
                element_text = price.text
                if element_text != "":
                    cost = int(element_text.split("-")
                               [1].strip().replace(",", ""))
                    item_prices.append(cost)

            # Create dictionary of store items and prices
            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            # Get current cookie count
            money_element = driver.find_element_by_id("money").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

            # Find upgrades that we can currently afford
            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id

            # Purchase the most expensive affordable upgrade
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element_by_id(to_purchase_id).click()

            # Add another 5 seconds until the next check
            time_out = time.time() + 5
    cps = driver.find_element(by=By.ID, value="cps")
    print(cps.text)
    driver.quit()


if __name__ == '__main__':
    main()
