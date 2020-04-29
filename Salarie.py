from Subsidiaries import *

class Salarie(Subsidiaries):
    def __init__(self,id,name,surname,wage,country):
        self._id = id
        self._name = name
        self._surname = surname
        self._wage = wage
        self._country = country

    def print(self):
        print(f"{self.__name} est composé de {len(self.__salarie)} salariés")
