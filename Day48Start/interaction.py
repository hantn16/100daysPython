from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "C:\Development\chromedriver"


def auto_input():
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("http://secure-retreat-92358.herokuapp.com/")
    first_name = driver.find_element(by=By.NAME, value='fName')
    first_name.send_keys("Han")
    last_name = driver.find_element(by=By.NAME, value='lName')
    last_name.send_keys("Trinh")
    email = driver.find_element(by=By.NAME, value='email')
    email.send_keys("hantn16@gmail.com")
    submit_btn = driver.find_element(by=By.CSS_SELECTOR, value='form button')
    submit_btn.click()
    driver.close()


def main():
    # service = Service(chrome_driver_path)
    # driver = webdriver.Chrome(service=service)
    # driver.get("https://en.wikipedia.org/wiki/Main_Page")
    # article_number = int(driver.find_element(
    #     by=By.CSS_SELECTOR,
    #     value='#articlecount>a').text.strip().replace(",", ""))
    # print(article_number)
    # driver.quit()
    auto_input()


if __name__ == '__main__':
    main()
