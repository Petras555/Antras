import math
import logging

logging.basicConfig(filename='logfailas.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

a = 10
b = 15
c = "25"
d = "asgasg"
x = 40
y = 0
def suma(*args):
    rez = 0
    for arg in args:
        rez += arg
    return rez

def saknis(c):
    sak = None
    try:
        sak = math.sqrt(c)
    except TypeError:
        logging.exception("Stringas, ne skaicius")
    else:
        return sak

def simboliu_sk(d):
    simb_sk=len(d)
    return simb_sk

def dalyba(x, y):
    dal = None
    try:
        dal = x / y
    except ZeroDivisionError:
        logging.exception("Dalyba is nulio")
    else:
        return dal

sudetis = suma(a, b)
pakelta_saknis = saknis(c)
ilgis = simboliu_sk(d)
padalinimas = dalyba(x, y)

logging.info(f"Sudetis: {a} + {b} = {sudetis} \n Saknis: sqrt({c}) = {pakelta_saknis} \n ilgis = len{d} = {ilgis} \n Dalyba: {x} / {y} = {padalinimas}  ")






