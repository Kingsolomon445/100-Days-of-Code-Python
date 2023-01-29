import requests
from bs4 import BeautifulSoup
import smtplib

EMAIL = "PUT YOUR EMAIL HERE"
PASSWORD = "PASS WORD"  # You have to create an app password to use here. Don't use the regular pass
LINK = 'https://www.amazon.com/dp/B0086ANRGU/ref=syn_sd_onsite_desktop_170?ie=UTF8&psc=1&pd_rd_plhdr=t'

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "PUT YOUR BROWSER USER AGENT HERE "
}
response = requests.get(
    LINK,
    headers=headers)
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')

price_whole = int(soup.find('span', class_='a-price-whole').get_text().rstrip('.'))
price_decimal= int(soup.find('span', class_='a-price-fraction').get_text().strip(''))
product_name = soup.find('span', id='productTitle').get_text().strip()
print(product_name)
print(price_whole)
print(price_decimal)


if price_whole < 100:
    with smtplib.SMTP("smtp.gmail.com") as conn:  # and if not gmail, look for their server and replace
        conn.starttls()  # makes our connection secure
        conn.login(user=EMAIL, password=PASSWORD)
        conn.sendmail(from_addr=EMAIL, to_addrs="receiver email",
                      msg=f"Price alert bot detected that the price for {product_name} is currently at "
                          f"${price_whole}.{price_decimal} \nYou can buy here: {LINK}")

