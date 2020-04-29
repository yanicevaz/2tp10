from Salarie import *

class Employee(Salarie):
    def __init__(self,id,name,surname,wage,country,hiringYear,numberDaysWorking):
        Salarie.__init__(self,id,name,surname,wage,country)
        self._hiringYear = hiringYear
        self._numberDaysWorking = numberDaysWorking

    def print(self):
        pass
