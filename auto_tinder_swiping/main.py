from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "C:\Development\chromedriver"
FB_EMAIL = "hantn16@gmail.com"
FB_PASSWORD = os.environ.get("FB_PASSWORD")
COCCOC_DIRECTORY = os.environ.get("COCCOC_DIRECTORY")


def main():
    autolike = input("Do you want to auto like? (y/n) ").lower() == "y"
    service = Service(chrome_driver_path)
    chrome_options = Options()
    print(COCCOC_DIRECTORY)
    chrome_options.binary_location = COCCOC_DIRECTORY
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://tinder.com/")
    sleep(2)
    login_button = driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')

    # '//*[@id="o-1556761323"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]'
    login_button.click()
    sleep(2)
    try:
        fb_login_btn = driver.find_element(
            by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_login_btn.click()
    except NoSuchElementException:
        more_option_btn = driver.find_element(
            by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div[3]/span/button')
        more_option_btn.click()
        fb_login_btn = driver.find_element(
            by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
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
    sleep(3)
    # Allow cookies
    cookies = driver.find_element(
        by=By.XPATH,
        value='/html/body/div[1]/div/div[2]/div/div/div[1]/button')
    cookies.click()
    sleep(3)
    # Allow location
    allow_location_button = driver.find_element(
        by=By.XPATH,
        value='/html/body/div[2]/div/div/div/div/div[3]/button[1]')
    allow_location_button.click()
    sleep(3)
    # Disallow notifications
    notifications_button = driver.find_element(
        by=By.XPATH,
        value='/html/body/div[2]/div/div/div/div/div[3]/button[2]')
    notifications_button.click()
    sleep(3)
    # Dismiss Vacinates
    try:
        vaccinated_button = driver.find_element(
            by=By.XPATH,
            value='/html/body/div[2]/div/div/div[1]/div[3]/button[2]')
        vaccinated_button.click()
        sleep(2)
    except NoSuchElementException:
        sleep(2)

    # Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
    for n in range(100):

        # Add a 1 second delay between likes.
        sleep(2)

        if autolike:
            try:
                like_button = driver.find_element(
                    by=By.XPATH,
                    value='//span[text()="Like"]/ancestor::button')

                like_button.click()
            except NoSuchElementException:
                # If out of potential matches
                try:
                    go_global_button = driver.find_element(
                        by=By.XPATH,
                        value='//span[text()="Go Global"]/parent::button')

                except NoSuchElementException:
                    sleep(1)
                else:
                    sleep(1)
                    break
            except ElementClickInterceptedException:
                try:
                    add_to_homescreen_button = driver.find_element(
                        by=By.XPATH,
                        value='//button[@data-testid="addToHomeScreen"]')
                except NoSuchElementException:
                    sleep(1)
                else:
                    not_interested_button = driver.find_element(
                        by=By.XPATH,
                        value='//span[text()="Not interested"]/parent::button')
                    not_interested_button.click()
                    continue
                # If out of potential matches
                try:
                    go_global_button = driver.find_element(
                        by=By.XPATH,
                        value='//span[text()="Go Global"]/parent::button')

                except NoSuchElementException:
                    sleep(1)
                else:
                    sleep(1)
                    break
                # If you're out of likes
                try:
                    out_of_likes_h3 = driver.find_element(
                        by=By.XPATH,
                        value='//h3[contains(text(),"Out of Likes!")]')
                except NoSuchElementException:
                    sleep(1)
                else:
                    nothanks_button = driver.find_element(
                        by=By.XPATH,
                        value="//span[text()='No Thanks']/parent::button")
                    nothanks_button.click()
                    sleep(2)
                    continue
                try:
                    backto_tinder_button = driver.find_element(
                        by=By.XPATH,
                        value='//button[@title="Back to Tinder"]')
                except NoSuchElementException:
                    sleep(1)
                else:
                    backto_tinder_button.click()
                    sleep(2)
                    continue
        else:
            try:
                dislike_button = driver.find_element(
                    by=By.XPATH,
                    value='//span[text()="Nope"]/ancestor::button')
                dislike_button.click()
            except ElementNotInteractableException:
                dislike_button = driver.find_element(
                    by=By.XPATH,
                    value='/html/body/div[2]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
                dislike_button.click()
            except NoSuchElementException:
                dislike_button = driver.find_element(
                    by=By.XPATH,
                    value='/html/body/div[2]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
                dislike_button.click()

    driver.quit()


if __name__ == '__main__':
    main()
