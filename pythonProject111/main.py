from tkinter import *

langas =Tk()

langas.geometry("250x250")
atmintis = []


def daryti(veiksmas):
    status["text"] = f" {veiksmas}                   "

def spausdinti(event):
    vardas = laukas1.get()
    tekstas ["text"] = f"Labas, {vardas}"
    atmintis.clear()
    atmintis.append(vardas)
    daryti("Sukurta                   ")




meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)

def isvalyti():
    tekstas ["text"] = " "
    daryti("Išvalyta                   ")

def atkurti():
    tekstas["text"] = f"Labas, {atmintis}"
    daryti("Atkurta                   ")
def iseiti(e):
    langas.quit()



meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

laukas1 = Entry(langas)
uzrasas = Label(langas, text="Įveskite vardą: ")
button = Button(langas, text="Įvesti")
tekstas = Label(langas, text="")

button.bind("<Button>", spausdinti)
langas.bind("<Return>", spausdinti)
langas.bind("<Escape>", lambda e: iseiti(e))


uzrasas.grid(row=0, column=0, sticky=E)
laukas1.grid(row=0, column=1)
button.grid(row=0, column=2, sticky=W)
tekstas.grid(row=1, columnspan=3)


status = Label(langas, text="                                 ", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=5, columnspan=10)











langas.mainloop()
