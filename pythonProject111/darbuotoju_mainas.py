import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///darbuotojai.db')
Base = declarative_base()


class Darbuotojas(Base):
    __tablename__ = 'Darbuotojas'
    id = Column(Integer, primary_key=True)
    name = Column('Vardas', String)
    surname = Column('Pavarde', String)
    birthday = Column('Gimimo data', String)
    pareigos  = Column('Pareigos', String)
    alga = Column('Atlyginimas', Float)
    start_date = Column('Darbo pradzios data', DateTime, default=datetime.datetime.now)

    def __init__(self, name, surname, birthday, pareigos, alga):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.pareigos = pareigos
        self.alga = alga

    def __repr__(self):
        return f'{self.id} {self.name} {self.surname}, {self.birthday}: {self.pareigos} {self.alga}  {self.start_date}'


Base.metadata.create_all(engine)