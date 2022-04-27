from tkinter import *


langas =Tk()

langas.geometry("750x750")
atmintis = StringVar()



# def spausdinti(event):
#     vardas = laukas1.get()
#     tekstas ["text"] = f"Labas, {vardas}"
#     atmintis.set(vardas)





def iseiti(e):
    langas.quit()





# laukas1 = Entry(langas)
uzrasas = Label(langas, text="Pasirinkite funkciją: ")
button1 = Button(langas, text="Atvaizduoti")
button2 = Button(langas, text="Prideti")
button3 = Button(langas, text="Pakeisti")
button4 = Button(langas, text="Istrinti")
button5 = Button(langas, text="Iseiti")
tekstas = Label(langas, text="")

# button.bind("<Button>", spausdinti)
# langas.bind("<Return>", spausdinti)
langas.bind("<Escape>", lambda e: iseiti(e))

uzrasas.grid(row=0, column=0, sticky=E)
# laukas1.grid(row=0, column=1)
button1.grid(row=0, column=2, sticky=W)
button2.grid(row=1, column=2, sticky=W)
button3.grid(row=2, column=2, sticky=W)
button4.grid(row=3, column=2, sticky=W)
button5.grid(row=4, column=2, sticky=W)
tekstas.grid(row=1, columnspan=3)



langas.mainloop()