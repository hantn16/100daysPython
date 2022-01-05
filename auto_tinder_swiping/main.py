from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "C:\Development\chromedriver"
FB_EMAIL = "hantn16@gmail.com"
FB_PASSWORD = os.environ.get("FB_PASSWORD")


def main():
    service = Service(chrome_driver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Users\Admin\AppData\Local\CocCoc\Browser\Application\browser.exe"
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
    driver.get("https://tinder.com/")
    sleep(2)
    login_button = driver.find_element(
        by=By.XPATH, value='//*[@id="o-1556761323"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')

    login_button.click()
    sleep(2)
    try:
        fb_login_btn = driver.find_element(
            by=By.XPATH, value='//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_login_btn.click()
    except NoSuchElementException:
        more_option_btn = driver.find_element(
            by=By.XPATH, value='//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/button')
        more_option_btn.click()
        fb_login_btn = driver.find_element(
            by=By.XPATH, value='//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_login_btn.click()

    # Switch to Facebook login window
    sleep(2)
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print(driver.title)

    # Login and hit enter
    email = driver.find_element(By.XPATH, '//*[@id="email"]')

    password = driver.find_element(By.XPATH, '//*[@id="pass"]')
    email.send_keys(FB_EMAIL)
    sleep(2)
    password.send_keys(FB_PASSWORD)
    sleep(2)
    password.send_keys(Keys.ENTER)

    # Switch back to Tinder window
    driver.switch_to.window(base_window)
    print(driver.title)

    driver.quit()


if __name__ == '__main__':
    main()
