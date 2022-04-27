import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('irasas.log')
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(message)s')

file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def iseiti():
    raise SystemExit

def prideti_irasa():
    memory = ""
    while True:
        pasirinkimas = int(input("Iveskite 1, jei norite prideti irasa \nIveskite 2, jei norite iseiti\n"))
        if pasirinkimas == 1:
            memory = input("iveskite irasa: ")
            logger.info(f"Ivestas irasas: {memory}")
        if pasirinkimas == 2:
            iseiti()

prideti_irasa()

# memory = ""
# while True:
#     pasirinkimas = int(input("Iveskite 1, jei norite prideti irasa; \nIveskite 2, jei norite iseiti"))
#     if pasirinkimas == 1:
#         memory = input("iveskite irasa: ")
#         logger.info(f"Ivestas irasas: {memory}")
#     if pasirinkimas == 2:
#         iseiti()