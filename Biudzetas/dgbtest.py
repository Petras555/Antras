class Namas:
    def __init__(self, verte, plotas):
        self.__verte = verte
        self.plotas = plotas

    @property
    def verte(self):
        return self.__verte
    @verte.setter
    def verte(self, naujas):


pirtnamis = Namas(0, "50kv.m.")

pirtnamis.verte()
print(type(pirtnamis.verte))
print(pirtnamis.verte)

