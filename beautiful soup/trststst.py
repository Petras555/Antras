import csv
import drys
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.elektrum.lt/lt/namams/elektra').text
soup = BeautifulSoup(source, 'html.parser')


test = soup.find_all('div', {'type': 'text/javascript'})
for t in test:
    print(t)
# script_blocks = soup.find_all('script', {'type': 'text/javascript'})
# special_code = ''
# for s in script_blocks:
#     if s.text.strip().startswith('price'):
#         special_code = s.text
#         break

# print(special_code)


# source = requests.get('https://www.elektrum.lt/lt/namams/elektra').text
# soup = BeautifulSoup(source, 'html.parser')
#
# print(soup.prettify())




# blokai = soup.find('div data-v-76720613', class_="ss-product-price-info single-zone")
#
# print(blokai)


# kategorijos = blokai.find_all('a', class_="mobiles-product-card__title js-open-product")
# with open('rageliai.csv', 'w', encoding='UTF-8', newline='') as failas:
#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['Modelis', 'Kaina'])
#     for blokas in blokai:
#         try:
#             ragelis = blokas.find('a', class_="mobiles-product-card__title js-open-product").text.strip()
#             # print(ragelis)
#             # modeliai.append(ragelis)
#             kainos_kategorija = blokas.find('div', class_="mobiles-product-card__full-price price")
#             kaina = kainos_kategorija.find('div', class_="mobiles-product-card__price-marker").text.strip()
#             # print(kaina)
#             csv_writer.writerow([ragelis, kaina])
#
#             # kainos.append(kaina)
#         except:
#             pass

# print(modeliai)
# print(kainos)
# with open('felfi.csv', 'w', encoding='UTF-8', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow()(['Kategorija', 'Textas'])
# for blokas in blokai:
    # try:
        # kategorija = blokas.find('div', class_='list-wrapper').text.strip()
# kategorija = blokai.find('a', class_='title')
# textas = kategorija.find_all('#text')
#
# for kat in textas:
#     print(kat.text.strip())
#
#     # except AttributeError:
#     #     pass
