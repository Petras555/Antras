from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from gfn import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()

while True:

    pasirinkimas = int(input("""Pasirinkite varianta: 
    1 - atvaidzuoti projektus
    2 - sukurti projektus
    3 - pakeisti projekta
    4 - istrinti projekta
    """))

    if pasirinkimas == 1:
        projektai = session.query(Projektas).all()
        print('-------------')
        for projektas in projektai:
            print(projektas)
        print('------------------')

    if pasirinkimas == 2:
        name = input('Iveskit projekto pavadinima: ')
        price = float(input('Iveskite projekto kaina: '))
        projektas = Projektas(name, price)
        session.add(projektas)
        session.commit()

    if pasirinkimas == 3:
        projektai = session.query(Projektas).all()
        print('-------------')
        for projektas in projektai:
            print(projektas)
        print('------------------')
        keiciamas_id = int(input("iveskite norimo pakeisti projekto ID: "))
        keiciamas_projektas = session.query(Projektas).filter_by(id=keiciamas_id)
        pakeitimas = int(input("Ka norite pakeist? 1-Name, 2-Price"))
        if pakeitimas == 1:
            keiciamas_projektas.name = input("Iveskite nauja projekto pavadinima: ")
        if pakeitimas == 2:
            keiciamas_projektas.price = float(input("Iveskite nauja projekto kaina: "))
        session.commit()

    if pasirinkimas == 4:
        projektai = session.query(Projektas).all()
        print('-------------')
        for projektas in projektai:
            print(projektas)
        print('------------------')
        trinamas_id = int(input("iveskite norimo pakeisti projekto ID: "))
        trinamas_projektas = session.query(Projektas).filter_by(id=trinamas_id).one()
        session.delete(trinamas_projektas)
        session.commit()



