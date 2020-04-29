from Multinationale import *

class Subsidiaries(Multinationale):
    def __init__(self,name, country, creationDate):
        self._name = name
        self._country = country
        self.creationDate = creationDate
        self._salarie = []

    def addSalarie(self,salarie):
        self._salarie.append(salarie)

    def supprSalarie(self,salarie):
        self._salarie.remove(salarie)

    def getCreationDate(self):
        return self.creationDate

    def getName(self):
        return self._name

    def getNbreSalaries(self):
        return len(self._salarie)

    def print(self):
        print(f"--{self._name} est composée de {len(self._salarie)} salariés")
        for i in self._salarie:
            i.print()

