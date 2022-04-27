import csv

from bs4 import BeautifulSoup
import requests

suma =0


source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')







blokai = soup.find_all('a', class_="CBarticleTitle")

for blokas in blokai:

    print(blokas)
    suma += 1

print(f"Is viso yra {suma} antrasciu")
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





