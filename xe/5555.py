import csv

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


#
# suma =0
#
url ="https://www.elektrum.lt/lt/namams/elektra"
source = requests.get(url)
soup = BeautifulSoup(source.text, 'html.parser')

driver =webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get(url)
driver.implicitly_wait(0.5)

l =driver.find_element_by_xpath("//button[text()='Nesutinku su slapukais']")

l.click()


html =driver.execute_script("return document.documentElement.outerHTML")
sel_soup =BeautifulSoup(html, 'html.parser')
print(sel_soup.findAll())



# driver = webdriver.Firefox()
# driver.get("https://www.elektrum.lt/lt/namams/elektra")
# print(soup.prettify())

# blokai = soup.find_all('div', class_="tm_pb_blurb_content")

# for blokas in blokai:
#     try:
#         ragelis = blokas.find('h3', style="color: #1ecf77;").text.strip()
#         print(ragelis)
#         # modeliai.append(ragelis)
#         # kainos_kategorija = blokas.find('div', class_="mobiles-product-card__full-price price")
#         # kaina = kainos_kategorija.find('div', class_="mobiles-product-card__price-marker").text.strip()
#         # print(kaina)
#
#
#         # kainos.append(kaina)
#     except:
#         pass