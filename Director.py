from Salarie import *

class Director(Salarie):
    def __init__(self, id,name, surname,wage,country, nominationYear):
        Salarie.__init__(self,id,name,surname,wage,country)
        self._nominationYear = nominationYear

    def print(self):
        print(f"* [id={self._id}] Nom et Prenom : {self._name} {self._surname}, Salaire : {self._wage}, Statut : Directeur, Année de nomination : {self._nominationYear}, Site : {self._country}")
