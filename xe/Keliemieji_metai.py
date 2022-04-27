from tkinter import *


langas = Tk()

langas.geometry("250x250")
langas.title("Keliemieji metai")
langas.iconbitmap(r'exek.ico')
metai1 = IntVar()
metai2 = IntVar()
listas = []


# metai = int(input("Iveskite pradinius metus: "))
# metai2 = int(input("Iveskite baigiamus metus: "))
# skirtumas = metai2 - metai
# for i in range(metai, metai2):
#     if (i % 400 == 0) or (i % 100 != 0 and i % 4 == 0):
#         print(f"{i} Keliamieji metai")
#     else:
#         print(f"{i} Nekeliamieji")

def metu_ivedimas1():

    ivestis = metu_irasas1.get()
    try:
        ivestis_int = int(ivestis)
        status['text'] = f"Ivesti {ivestis_int} metai"
        metai1.set(ivestis_int)
    except:
        status['text'] = "Blogai ivesti metai"




def metu_ivedimas2():
    ivestis = metu_irasas2.get()
    try:
        ivestis_int = int(ivestis)
        status['text'] = f"Ivesti {ivestis_int} metai"
        metai2.set(ivestis_int)
    except:
        status['text'] = "Blogai ivesti metai"



def skaiciuokle():
    for i in range(metai1, metai2):
        if (i % 400 == 0) or (i % 100 != 0 and i % 4 == 0):
            listas.append(i)

def skaiciuoti_rezultata():
    pirmi = metai1.get()
    antri = metai2.get()

    if pirmi > antri:
        status['text'] = "Blogai ivesti metai"
        return None
    if pirmi == 0 or antri == 0:
        status['text'] = "Neivesti metai"
        return None
    for i in range(pirmi, antri):
        if (i % 400 == 0) or (i % 100 != 0 and i % 4 == 0):
            listas.append(i)
            if len(listas) % 10 ==0:
                listas.append("\n")
    rezultatas['text'] = listas

metu_irasas1 = Entry(langas)
metu_irasas2 = Entry(langas)
mygtukas_irasui1 =Button(langas, text="Ivesti", command=metu_ivedimas1)
mygtukas_irasui2 =Button(langas, text="Ivesti", command=metu_ivedimas2)
mygtukas_rezultatui =Button(langas, text="Skaiciuoti keliamuosius metus", command=skaiciuoti_rezultata)
rezultatas = Label(langas, text="dddd")
status = Label(langas, text='      ', relief=SUNKEN, anchor=W,)

# mygtukas_irasui1.bind("<Button-1>", lambda e: metu_ivedimas1())
# mygtukas_irasui2.bind("<Button-2>", lambda e: metu_ivedimas2())

metu_irasas1.grid(row=1, column=0)
metu_irasas2.grid(row=3, column=0)
mygtukas_irasui1.grid(row=1, column=1)
mygtukas_irasui2.grid(row=3, column=1)
mygtukas_rezultatui.grid(row=4, column=0)
rezultatas.grid(rowspan=8,columnspan=2)
status.grid(row=50, columnspan=5)







langas.mainloop()