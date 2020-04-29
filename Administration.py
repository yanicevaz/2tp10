from Employee import *

class Administration(Employee):
    def __init__(self,id,name,surname,wage,country,hiringYear,numberDaysWorking,service):
        Employee.__init__(self,id,name,surname,wage,country,hiringYear,numberDaysWorking)
        self.__service = service

    def print(self):
        print(f"* [id={self._id}] Nom et Prenom : {self._name} {self._surname}, Salaire : {self._wage}, Statut : Administratif, Année d'embauche : {self._hiringYear}, Site : {self._country}, Nombre de jours de travail : {self._numberDaysWorking}, Service : {self.__service}")
