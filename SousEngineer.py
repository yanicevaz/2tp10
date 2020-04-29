from Engineer import *

class Junior(Engineer):
    def __init__(self,id,name,surname,wage,country,hiringYear,numberDaysWorking,nbHoursProject,nbHoursGestion,nbExpYears):
        Engineer.__init__(self,id,name,surname,wage,country,hiringYear,numberDaysWorking,nbHoursProject,nbHoursGestion)
        self.__nbExpYears = nbExpYears

    def print(self):
        print(f"* [id={self._id}] Nom et Prenom : {self._name} {self._surname}, Salaire : {self._wage}, Statut : Ingénieur-junior, Année d'embauche : {self._hiringYear}, Site : {self._country}Nombre de jours de travail : {self._numberDaysWorking}, Nombre d'heures de gestion : {self._nbHoursGestion}, Nombre d'heures de projet : {self._nbHoursProject}, Nombre d'années d'expérience : {self._nbExpYears}")

class Senior(Engineer):
    def __init__(self,id,name,surname,wage,country,hiringYear,numberDaysWorking,nbHoursProject,nbHoursGestion,responsability):
        Engineer.__init__(self,id,name,surname,wage,country,hiringYear,numberDaysWorking,nbHoursProject,nbHoursGestion)
        self.__responsability = responsability

    def print(self):
        print(f"* [id={self._id}] Nom et Prenom : {self._name} {self._surname}, Salaire : {self._wage}, Statut : Ingénieur-senior, Année d'embauche : {self._hiringYear}, Site : {self._country} Nombre de jours de travail : {self._numberDaysWorking}, Nombre d'heures de gestion : {self._nbHoursGestion}, Nombre d'heures de projet : {self._nbHoursProject}, Responsabilité : {self.__responsability}")
