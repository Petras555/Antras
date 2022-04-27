# from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.enefit.lt/lt/privatiems/elektra'

r = session.get(url)

r.html.render(sleep=5, keep_page=True, scrolldown=3)

kaina = r.html.find('#tariff-product__price-number tariff-product__price-number--small')

for i in kaina:
    x = {
        'span': item.text,
         }
    print(x)


# soup = BeautifulSoup(source, 'html.parser')
#
# # print(soup.prettify())
#
# blokai = soup.find_all('div', class_="flex flex--left flex--tight")
#
# for blokas in blokai:
#     kategorija = blokas.find('span', class_="tariff-product__price-number tariff-product__price-number--small").text
#     print(kategorija)




























# from tkinter import *
#
# langas = Tk()
#
# virsutinis = Frame(langas)
# apatinis = Frame(langas)
#
# mygtukas1 = Button(virsutinis, text="1 mygtukas")
# mygtukas2 = Button(virsutinis, text="2 mygtukas")
# mygtukas3 = Button(virsutinis, text="3 mygtukas")
# mygtukas4 = Button(apatinis, text="4 mygtukas")
#
# virsutinis.pack()
# apatinis.pack(side=BOTTOM)
# mygtukas1.pack(side=LEFT)
# mygtukas2.pack(side=LEFT)
# mygtukas3.pack(side=LEFT)
# mygtukas4.pack(side=BOTTOM, fill=Y)
#
# langas.mainloop()