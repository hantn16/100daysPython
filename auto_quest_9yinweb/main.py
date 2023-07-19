from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_driver_path = "C:\Development\chromedriver.exe"
FB_EMAIL = "hantn16@gmail.com"
FB_PASSWORD = os.environ.get("FB_PASSWORD")
CHROME_DIRECTORY = "C:\Program Files\Google\Chrome\Application\chrome.exe"


def run_9yinweb(user9yin,userfb='ngayradi01@gmail.com'):
    # autolike = input("Do you want to auto like? (y/n) ").lower() == "y"
    service = Service(executable_path=chrome_driver_path)
    chrome_options = Options()
    chrome_options.binary_location = CHROME_DIRECTORY
    driver = webdriver.Chrome(options=chrome_options,service=service)
    # Setup wait for later
    wait = WebDriverWait(driver, 10)
    driver.get("https://cuuam.gosu.vn/home/su-kien/thap-nien-trung-phung.htm")
    original_window = driver.current_window_handle
    # Login and hit enter
    sleep(2)
    login_button = driver.find_element(
        by=By.XPATH, value='/html/body/div[9]/div[6]/div[1]/div/div[1]')
    login_button.click()
    sleep(2)
    iframe = driver.find_element(By.CLASS_NAME, "gosu-popup-iframe")
    driver.switch_to.frame(iframe)
    user = driver.find_element(By.XPATH,'//*[@id="tablePopup2"]/tbody/tr[1]/td/input')
    password = driver.find_element(By.XPATH, '//*[@id="tablePopup2"]/tbody/tr[3]/td/input')
    sleep(2)
    user.send_keys(user9yin)
    sleep(1)
    password.send_keys('anhhan16')
    sleep(1)
    password.send_keys(Keys.ENTER)
    sleep(2)
    #Bao danh
    btn_baodanh = driver.find_element(By.XPATH,'//*[@id="btn-share"]')
    btn_baodanh.click()
    sleep(2)
    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))
    
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    fb_user = driver.find_element(By.XPATH,'//*[@id="email"]')
    sleep(2)
    fb_user.send_keys(userfb)
    
    fb_password = driver.find_element(By.XPATH,'//*[@id="pass"]')
    sleep(2)
    fb_password.send_keys('anhhan16')
    sleep(2)
    fb_password.send_keys(Keys.ENTER)
    sleep(5)
    print(len(driver.window_handles))
    btn_share = driver.find_element(By.NAME,'__CONFIRM__')
    btn_share.click()
    sleep(10)
    #Close the tab or window
    driver.close()

    #Switch back to the old tab or window
    driver.switch_to.window(original_window)
    #Nhan luot
    btn_nhanluot = driver.find_element(By.XPATH,'//*[@id="vuotai"]/div[2]/div[2]/div[2]')
    btn_nhanluot.click()
    sleep(3)
    btn_traqmoingay = driver.find_element(By.XPATH,'//*[@id="popup-mission"]/div/div/div[2]/div/div/div[2]/div[2]')
    if btn_traqmoingay.text == 'NHẬN':
        btn_traqmoingay.click()
        sleep(3)
    # btn_traqbaodanh = driver.find_element(By.XPATH,'//*[@id="popup-mission"]/div/div/div[2]/div/div/div[3]/div[2]')
    # if btn_traqbaodanh.text == 'NHẬN':
    #     btn_traqbaodanh.click()
    #     sleep(3)
    try:
        btn_xemvideo = driver.find_element(By.XPATH,'//*[@id="popup-mission"]/div/div/div[2]/div/div/div[5]/a')
        if btn_xemvideo.text == 'XEM':
            btn_xemvideo.click()
            sleep(7)
    except NoSuchElementException:
        pass
    if len(driver.window_handles) > 1:
            # Loop through until we find a new window handle
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                driver.close()
                driver.switch_to.window(original_window)
                break

    sleep(2)
    # try:
    #     btn_sharetin = driver.find_element(By.XPATH,'//*[@id="popup-mission"]/div/div/div[2]/div/div/div[4]/div[2]')
    #     if btn_sharetin.text == 'CHIA SẺ':
    #         btn_sharetin.click()
    #         sleep(3)
    #         for window_handle in driver.window_handles:
    #             if window_handle != original_window:
    #                 driver.switch_to.window(window_handle)

    #                 break
    #         btn_share_bd = driver.find_element(By.NAME,'__CONFIRM__')
    #         btn_share_bd.click()
    #         sleep(5)
    # except:
    #     pass
    driver.quit()
def main():
    for i in range (30):
        run_9yinweb('s20theguy'+str(i+1).zfill(2))

if __name__ == '__main__':
    main()
