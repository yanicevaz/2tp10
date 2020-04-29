class Multinationale :
    def __init__(self,name,countryOrigin):
        self.__name=name
        self.__countryOrigin=countryOrigin
        self.__subsidiaries=[]

    def addSubsidiaries(self,subisdiaries):
        self.__subsidiaries.append(subisdiaries)

    def print(self):
        print(f"La multinationale {self.__name} est composé de {len(self.__subsidiaries)} filiales. Son pays d'origine est : {self.__countryOrigin}.")



        nbsalarie = 0
        for i in self.__subsidiaries:
            nbsalarie += len(i._salarie)
        print(f"{self.__name} est composé de {nbsalarie} salariés :")

        for i in self.__subsidiaries:
            i.print()

        """temporary = 1000
        counter = 0
        numeroSub = 0
        total = 0
        for i in self.__subsidiaries:
            dateSub = i.getCreationDate()
            total += (self.__subsidiaries[counter]).getNbreSalaries
            if dateSub < temporary:
                temporary = dateSub
                numeroSub = counter

            counter += 1
        oldest = (self.__subsidiaries[numeroSub]).getName()
        nbreEmployees = (self.__subsidiaries[numeroSub]).getNbreSalaries()

        print(f"- La multionationale {self.__name} est composé de {len(self.__subsidiaries)} filiales. Son pays d'origine est {self.__countryOrigin}")
        for i in self.__subsidiaries:
            i.print()"""
