from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "C:\Development\chromedriver"


def main():
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    article_number = int(driver.find_element(
        by=By.CSS_SELECTOR,
        value='#articlecount>a').text.strip().replace(",", ""))
    print(article_number)
    driver.quit()


if __name__ == '__main__':
    main()
