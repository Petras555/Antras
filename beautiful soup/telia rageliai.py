import csv

from bs4 import BeautifulSoup
import requests

suma =0


source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung').text
soup = BeautifulSoup(source, 'html.parser')

# print(soup.prettify())



modeliai = []
kainos = []

blokai = soup.find_all('div', class_="col-lg-4 col-sm-6 col-xs-12")
# kategorijos = blokai.find_all('a', class_="mobiles-product-card__title js-open-product")
with open('rageliai.csv', 'w', encoding='UTF-8', newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Modelis', 'Kaina'])
    for blokas in blokai:
        try:
            ragelis = blokas.find('a', class_="mobiles-product-card__title js-open-product").text.strip()
            # print(ragelis)
            # modeliai.append(ragelis)
            kainos_kategorija = blokas.find('div', class_="mobiles-product-card__full-price price")
            kaina = kainos_kategorija.find('div', class_="mobiles-product-card__price-marker").text.strip()
            # print(kaina)
            csv_writer.writerow([ragelis, kaina])

            # kainos.append(kaina)
        except:
            pass

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
