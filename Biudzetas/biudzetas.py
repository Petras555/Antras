from modules.biudzet import *


biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("""1.Pajamos 
2.Išlaidos 
3.Balansas 
4.Ataskaita 
9.Išeiti iš programos
    """))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamas: "))
        siuntejas = input("Siuntėjas: ")
        papildoma_informacija = input("Papildoma informacija: ")
        biudzetas.prideti_pajamas(suma, siuntejas, papildoma_informacija)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidas: "))
        atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
        isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
        biudzetas.prideti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
    if pasirinkimas == 3:
        biudzetas.gauti_balansą()
    if pasirinkimas == 4:
        biudzetas.gauti_ataskaita()
    if pasirinkimas == 9:
        break