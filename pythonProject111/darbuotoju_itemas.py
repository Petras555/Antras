from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from darbuotoju_mainas import Darbuotojas

engine = create_engine('sqlite:///darbuotojai.db')
Session = sessionmaker(bind=engine)
session = Session()

while True:

    pasirinkimas = int(input("""Pasirinkite varianta: 
    1 - atvaidzuoti darbuotojus
    2 - pridėti darbuotojus
    3 - atnaujinti darbuotojus
    4 - istrinti projekta
    """))

    if pasirinkimas == 1:
        darbuotojai = session.query(Darbuotojas).all()
        print('-------------')
        for darbuotojas in darbuotojai:
            print(darbuotojas)
        print('------------------')

    if pasirinkimas == 2:
        name = input('Iveskit darbuotojo varda: ')
        surname = input('Iveskit darbuotojo pavarde: ')
        birthday = input('Iveskit darbuotojo gimimo data: ')
        pareigos = input('Iveskite dabuotojo pargeigas: ')
        alga = float(input('Iveskite dabuotojo atlyginima: '))
        darbuotojas = Darbuotojas(name, surname, birthday, pareigos, alga)
        session.add(darbuotojas)
        session.commit()

    if pasirinkimas == 3:
        darbuotojai = session.query(Darbuotojas).all()
        print('-------------')
        for darbuotojas in darbuotojai:
            print(darbuotojas)
        print('------------------')
        keiciamas_id = int(input("iveskite norimo pakeisti darbuotojo ID: "))
        keiciamas_darbuotojas = session.query(Darbuotojas).get(keiciamas_id)
        pakeitimas = int(input("Ka norite pakeist? 1-Varda, 2-Pavarde, 3-Gim.data, 4-Pareigas, 5-Atlyginima. "))
        if pakeitimas == 1:
            keiciamas_darbuotojas.name = input("Iveskite nauja darbuotojo varda: ")
        if pakeitimas == 2:
            keiciamas_darbuotojas.surname = input("Iveskite nauja darbuotojo pavadinima: ")
        if pakeitimas == 3:
            keiciamas_darbuotojas.birthday = input("Iveskite nauja darbuotojo gimimo data: ")
        if pakeitimas == 4:
            keiciamas_darbuotojas.pareigos = input("Iveskite naujaa darbuotojo pareigas: ")
        if pakeitimas == 5:
            keiciamas_darbuotojas.alga = float(input("Iveskite nauja darbuotojo atlyginima: "))


    if pasirinkimas == 4:
        darbuotojai = session.query(Darbuotojas).all()
        print('-------------')
        for darbuotojas in darbuotojai:
            print(darbuotojas)
        print('------------------')
        trinamas_id = int(input("iveskite norimo panaikinti darbuotojo ID: "))
        trinamas_darbuotojas = session.query(Darbuotojas).filter_by(id=trinamas_id).one()
        session.delete(trinamas_darbuotojas)
        session.commit()


