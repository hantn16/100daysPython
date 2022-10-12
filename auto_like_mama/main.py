from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
chrome_driver_path = "C:\Development\chromedriver"
FB_EMAIL = "ngayradi01@gmail.com"
FB_PASSWORD = os.environ.get("FB_PASSWORD")
COCCOC_DIRECTORY = os.environ.get("COCCOC_DIRECTORY")


def main():
    service = Service(chrome_driver_path)
    chrome_options = Options()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://tbdhs.moet.gov.vn/storage/detail/1660015028994-31a67fb5-0439-4782-abd0-e4d2a58f5b26-7a13d53d-b1ea-4ec4-aafe-9ce03f70697b")
    for n in range(1000):
        email_address = f"ngaytrove{n+1}@gmail.com"
        sleep(1)
        like_button = driver.find_element(
            by=By.XPATH, value='/html/body/app-root/app-main-layout/div/app-digital-detail/div[1]/div[3]/div[1]/div[2]/div[2]/img')
        like_button.click()
        sleep(1)

        # Switch to Facebook login window
        sleep(1)
        # Login and hit enter
        email = driver.find_element(
            By.XPATH, '/html/body/app-root/app-main-layout/div/app-digital-detail/div[2]/div/div[2]/input')
        email.send_keys(email_address)
        sleep(1.5)
        accept_btn = driver.find_element(
            By.XPATH, '/html/body/app-root/app-main-layout/div/app-digital-detail/div[2]/div/div[3]/button')
        accept_btn.click()
        sleep(1)
        Alert(driver).accept()
        sleep(3)

    driver.quit()


if __name__ == '__main__':
    main()
