from Employee import *

class Engineer(Employee):
    def __init__(self,id,name,surname,wage,country,hiringYear,numberDaysWorking,nbHoursProject,nbHoursGestion):
        Employee.__init__(self,id,name,surname,wage,country,hiringYear,numberDaysWorking)
        self._nbHoursProject = nbHoursProject
        self._nbHoursGestion = nbHoursGestion

    def print(self):
        pass
