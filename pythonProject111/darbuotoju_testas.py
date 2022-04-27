from tkinter import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from darbuotoju_mainas import Darbuotojas

engine = create_engine('sqlite:///darbuotojai.db')
Session = sessionmaker(bind=engine)
session = Session()
langas =Tk()
test =""
tarpas = "\n"

langas.geometry("750x750")
langas.title("Duombazes tvarkykle")
atmintis = []
var = IntVar()
var2 = StringVar()
name5 = StringVar()
def ivestis():
    ivedimas = laukas1.get()

def atvaizdavimas(event):
    darbuotojai = session.query(Darbuotojas).all()
    for darbuotojas in darbuotojai:
        atmintis.append(darbuotojas)
        atmintis.append(tarpas)
        tekstas ["text"] = atmintis

    atmintis.clear()

def pridejimas(event):
    button6.wait_variable(var)
    status["text"] = "Iveskite varda: "
    name = name5.get()
    delete_entry()
    status["text"] = "Iveskite pavarde: "
    button6.wait_variable(var)
    surname = str(laukas1.get())
    delete_entry()
    status["text"] = "Iveskit darbuotojo gimimo data:  "
    button6.wait_variable(var)
    birthday = str(laukas1.get())
    delete_entry()
    status["text"] = "Iveskite dabuotojo pargeigas: "
    button6.wait_variable(var)
    pareigos = str(laukas1.get())
    delete_entry()
    status["text"] = "Iveskite dabuotojo atlyginima:  "
    button6.wait_variable(var)
    test = str(laukas1.get())
    print(test)
    print(type(test))
    alga = float(test)
    delete_entry()
    status["text"] = ""
    darbuotojas = Darbuotojas(name, surname, birthday, pareigos, alga)
    session.add(darbuotojas)
    session.commit()

def pakeitimas(event):
        darbuotojai = session.query(Darbuotojas).all()
        for darbuotojas in darbuotojai:
            atmintis.append(darbuotojas)
            atmintis.append(tarpas)
            tekstas["text"] = atmintis
        atmintis.clear()
        status["text"] = "iveskite norimo pakeisti darbuotojo ID: "
        button6.wait_variable(var)
        test = int(laukas1.get())
        keiciamas_darbuotojas = session.query(Darbuotojas).get(test)
        tekstas["text"] = session.query(Darbuotojas).get(test)
        delete_entry()
        status["text"] = "Ka norite pakeist? 1-Varda, 2-Pavarde, 3-Gim.data, 4-Pareigas, 5-Atlyginima. "
        button6.wait_variable(var)
        pasirinkimas = laukas1.get()
        if pasirinkimas == "1":
            delete_entry()
            status["text"] = "Iveskite nauja darbuotojo varda: "
            button6.wait_variable(var)
            keiciamas_darbuotojas.name = str(laukas1.get())
            delete_entry()
        if pasirinkimas == "2":
            delete_entry()
            status["text"] = "Iveskite nauja darbuotojo pavadinima:  "
            button6.wait_variable(var)
            keiciamas_darbuotojas.surname = str(laukas1.get())
            delete_entry()
        if pasirinkimas == "3":
            delete_entry()
            status["text"] = "Iveskite nauja darbuotojo gimtadieni:  "
            button6.wait_variable(var)
            keiciamas_darbuotojas.birthday = str(laukas1.get())
            delete_entry()
        if pasirinkimas == "4":
            delete_entry()
            status["text"] = "Iveskite nauja darbuotojo pareigas:  "
            button6.wait_variable(var)
            keiciamas_darbuotojas.pareigos = str(laukas1.get())
            delete_entry()
        if pasirinkimas == "5":
            delete_entry()
            status["text"] = "Iveskite nauja darbuotojo alga:  "
            button6.wait_variable(var)
            keiciamas_darbuotojas.alga = float(laukas1.get())
            delete_entry()

        else:
            status["text"] = "Blogai ivesta, pasirinkite is naujo  "

def istrinimas(event):
        darbuotojai = session.query(Darbuotojas).all()
        for darbuotojas in darbuotojai:
            atmintis.append(darbuotojas)
            atmintis.append(tarpas)
            tekstas["text"] = atmintis
        atmintis.clear()
        status["text"] = "iveskite norimo panaikinti darbuotojo ID: "
        button6.wait_variable(var)
        test = int(laukas1.get())
        trinamas_id = test
        trinamas_darbuotojas = session.query(Darbuotojas).filter_by(id=trinamas_id).one()
        session.delete(trinamas_darbuotojas)
        session.commit()
        atvaizdavimas(event)

def iseiti(e):
    langas.quit()

def funcA():
    x = laukas1.get()
    print(x)
    var.set(1)
    name5.set(x)


def delete_entry():
    laukas1.delete(0, 'end')


laukas1 = Entry(langas, textvariable=var2)
uzrasas = Label(langas, text="Pasirinkite funkciją: ")
button1 = Button(langas, text="Atvaizduoti")
button2 = Button(langas, text="Prideti")
button3 = Button(langas, text="Pakeisti")
button4 = Button(langas, text="Istrinti")
button5 = Button(langas, text="Iseiti")
button6 = Button(langas, text="Click Me", command=funcA)
tekstas = Label(langas, text="", height=15)

# button.bind("<Button>", spausdinti)
# langas.bind("<Return>", spausdinti)
button1.bind("<Button>", atvaizdavimas)
button2.bind("<Button>", pridejimas)
button3.bind("<Button>", pakeitimas)
button4.bind("<Button>", istrinimas)
button5.bind("<Button>", iseiti)
# langas.bind("<Escape>", lambda e: iseiti(e))


uzrasas.grid(row=0, column=0, sticky=E)
# laukas1.grid(row=0, column=1)
button1.grid(row=0, column=2, sticky=W)
button2.grid(row=1, column=2, sticky=W)
button3.grid(row=2, column=2, sticky=W)
button4.grid(row=3, column=2, sticky=W)
button5.grid(row=4, column=2, sticky=W)
tekstas.grid(row=7, columnspan=7, sticky=W)
laukas1.grid(row=0, column=5, sticky=E)
button6.grid(row=0, column=6, sticky=E)

status = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=8, columnspan=3, sticky=W+E)


langas.mainloop()
