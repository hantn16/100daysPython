from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "C:\Development\chromedriver"


def main():
    # Create a new Chrome session
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.python.org/")
    event_times = driver.find_elements(
        by=By.CSS_SELECTOR, value="div.event-widget time")
    event_names = driver.find_elements(
        by=By.CSS_SELECTOR, value="div.event-widget li a")
    my_dict = {}
    for i in range(len(event_times)):
        my_dict[i] = {
            "time": event_times[i].text,
            "name": event_names[i].text
        }
    print(my_dict)
    driver.quit()


if __name__ == '__main__':
    main()
