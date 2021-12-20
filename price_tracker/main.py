import lxml
import requests as req
import os
import smtplib
from bs4 import BeautifulSoup
URL = 'https://hoanghamobile.com/dien-thoai-di-dong/apple-iphone-13-pro-max-256gb-chinh-hang-vn-a'
my_email = "hantn.devx@gmail.com"


def send_emails(lst_address, subject, content, link):
    gmail_password = os.environ.get('GMAIL_PASSWORD')
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=gmail_password)
        conn.sendmail(from_addr=my_email, to_addrs=lst_address,
                      msg=f"Subject:{subject}\n\n{content}\n{link}".encode('utf-8'))


def main():
    res = req.get(url=URL)
    bs = BeautifulSoup(res.text, features='lxml')
    title = bs.select_one('div.top-product > h1').getText().strip()
    price_tag = bs.select_one('p.current-product-price>strong')
    price_text = price_tag.text.strip()
    price = int(price_text.split(' ')[0].replace(',', ''))
    if price <= 38000000:
        msg = f'{title} hiện có giá {price_text}'
        send_emails('hantn16@gmail.com', 'Iphone price alert🌟🌟🌟', msg, URL)


if __name__ == '__main__':
    main()
