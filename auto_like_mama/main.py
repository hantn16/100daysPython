from time import sleep
import os
import random as rd
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
# COCCOC_DIRECTORY = os.environ.get("COCCOC_DIRECTORY")
COCCOC_DIRECTORY = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
LS_HO = ["nguyen",
         "tran",
         "le",
         "pham",
         "hoang", "huynh", "vu", "vo", "phan", "truong", "bui", "dang", "do", "ngo", "ho", "duong", "dinh", "trinh"]
LS_TEN = ["xuanhan", "chilan", "thaohuong", "baotruc", "ngoctu", "han", "ngocoanh", "ngochoan", "anhthy", "thuthuy", "linhnhi", "tinhyen", "phuong", "ngochuyen", "gialinh", "maiha", "tramoanh", "xuanhanh", "nhahong", "nhatha", "hieuminh", "hoangphat", "quangkhai", "thedoanh", "honggiang", "ankhang", "tuongphat", "dangkhuong", "ducduy", "thedan", "thongnhat", "quochung", "dongquan", "quangbuu", "thebinh", "tanloi", "dangkhoa", "minhdanh", "minhtien", "tuankhang", "quoctoan", "minhkhanh", "baky", "haonhien", "xuanphuc", "kienbinh", "trungchinh", "khanhhai", "vietkhai", "quangthien", "nhatlinh", "truongchinh", "anhdung", "hiephao", "tuanngoc", "duchuy", "khactuan", "khaituan", "hoangdue",
          "thienkim", "baoduong", "thanhhang", "thanhloan", "ngoctrinh", "tuenhi", "minhthu", "huyenanh", "vangiang", "hongchau", "thuylinh", "thytruc", "thuyhong", "thienduyen", "maingocbich", "tranchau", "hoaithu", "quynhvan", "hoa", "thuhang", "xuanuyen", "kieudung", "ngochoan", "bichha", "thuytien", "andi", "ngocvy", "thuyminh", "quynhnhung", "thaichi", "habang", "thuyquynh", "viettuyet", "bichsan", "ngochang", "songoanh", "thuyminh", "nhatrang", "thuyen", "dieuanh", "quangdong", "trunganh", "namduong", "duccao", "thetuong", "trongkim", "baoduy", "dinhnhan", "thanhcong", "annguyen", "manhthang", "trihao", "quochuy", "giangthien", "quanghuy", "huuchien", "nhatquoc", "phihung", "giaphuoc", "sonquan"]
LS_MAIL_SERVER = ["gmail.com", "yahoo.com", "outlook.com"]


def random_email():
    style1 = f'{rd.choice(LS_HO)}{rd.choice([".",""])}{rd.choice(LS_TEN)}@{rd.choice(LS_MAIL_SERVER)}'
    style2 = f'{rd.choice(LS_HO)}{rd.choice([".",""])}{rd.choice(LS_TEN)}{rd.choice([".",""])}{rd.randint(1,99)}@{rd.choice(LS_MAIL_SERVER)}'
    style3 = f'{rd.choice(LS_TEN)}{rd.choice([".",""])}{rd.choice(LS_HO)}{rd.choice([".",""])}{rd.randint(1,99)}@{rd.choice(LS_MAIL_SERVER)}'
    style4 = f'{rd.choice(LS_TEN)}{rd.choice([".",""])}{rd.choice(LS_HO)}@{rd.choice(LS_MAIL_SERVER)}'
    return rd.choice([style1, style2, style3, style4])


def main():
    for n in range(1500):
        service = Service(chrome_driver_path)
        chrome_options = Options()
        chrome_options._binary_location = COCCOC_DIRECTORY
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://tbdhs.moet.gov.vn/storage/detail/1660015028994-31a67fb5-0439-4782-abd0-e4d2a58f5b26-7a13d53d-b1ea-4ec4-aafe-9ce03f70697b")
        email_address = random_email()
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
        sleep(2)

        driver.quit()


if __name__ == '__main__':
    main()
