from bs4 import BeautifulSoup
import requests
from collections import deque
import time
import smtplib

url_list = ['https://www.boots.com/the-ordinary-hyaluronic-acid-2-percent-and-b5-serum-60ml-10277845',
            'https://www.boots.com/the-ordinary-niacinamide-10-percent-and-zinc-1-percent-s-10277847']


def boots_deal(url):
    #
    for x in url:
        scrape = True
        print(x)
        while scrape:
            html_text = requests.get(x).text
            soup = BeautifulSoup(html_text, 'html.parser')
            nian = soup.find('div', class_='brand_the_ordinary')
            price = nian.find('div', class_='price price_redesign').text
            naked_price = price.replace("£", "")
            print(naked_price)
            set_price = None
            product_name = nian.find('div', id='estore_product_title').text


            if naked_price != set_price:
                if set_price is None:
                    int_scrape = True
                if int_scrape is True:
                    set_price = naked_price
                    while float(naked_price) < float(set_price) and int_scrape is False:
                        print(f"The current price of {product_name} at Boots is £{naked_price}")
                        print(f"Link to product: {x}")
                        set_price = naked_price
                        scrape = False
                        break
                else:
                    set_price = naked_price
                    int_scrape = False
                    break


#   product_price = 13.90

# url = 'https://www.boots.com/the-ordinary-hyaluronic-acid-2-percent-and-b5-serum-60ml-10277845'
#    html_text = requests.get(
#        'https://www.boots.com/the-ordinary-hyaluronic-acid-2-percent-and-b5-serum-60ml-10277845').text
#    soup = BeautifulSoup(html_text, 'html.parser')
#    nian = soup.find('div', class_='brand_the_ordinary')
#    price = nian.find('div', class_='price price_redesign').text
#    naked_price = price.replace("£", "")
#    product_name = nian.find('div', id='estore_product_title').text
#    while float(naked_price) != product_price:
#        print(f"The current price of {product_name} at Boots is £{naked_price}")
#        print(f"Link to product: {url}")
#        product_price = naked_price

#        break

# url = 'https://www.boots.com/the-ordinary-hyaluronic-acid-2-percent-and-b5-serum-60ml-10277845'
#    html_text = requests.get(
#        'https://www.boots.com/the-ordinary-hyaluronic-acid-2-percent-and-b5-serum-60ml-10277845').text
#    soup = BeautifulSoup(html_text, 'html.parser')
#    nian = soup.find('div', class_='brand_the_ordinary')
#    price = nian.find('div', class_='price price_redesign').text
#    naked_price = price.replace("£", "")
#    product_name = nian.find('div', id='estore_product_title').text
#    while float(naked_price) != product_price:
#        print(f"The current price of {product_name} at Boots is £{naked_price}")
#        print(f"Link to product: {url}")
#        product_price = naked_price

# break


boots_deal(url_list)

# smt = smtplib.SMTP('smtp.gmail.com', port=587)
# smt.ehlo()
# smt.starttls()
# smt.login('skincarepricealerts@gmail.com', 'ldbzxdxkmbuzvjdw')
# smt.sendmail('skincarepricealerts@gmail.com',
# 'skincarepricealerts@gmail.com',
# f"Subject: {product_name}\n\nHi, {product_name} has dropped to {naked_price}!\n\n"
# f"Here's the link: {url}")
# smt.quit()
# break


# if __name__ == '__main__':
# while True:
# boots_deal()
# time_wait = 86400
# time.sleep(time_wait * 60)
