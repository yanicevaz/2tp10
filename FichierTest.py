import Multinationale
import Subsidiaries
import Salarie
import Director
import Employee
import Administration
import Engineer
import SousEngineer



newMultinationale = Multinationale.Multinationale("RCAT", "FRANCE")

FilTun = Subsidiaries.Subsidiaries("RCAT-Tunisie","Tunisie",2012)
FilBel = Subsidiaries.Subsidiaries("RCAT-Belgique","Belgique",2016)
FilMar = Subsidiaries.Subsidiaries("RCAT-Maroc","Maroc",2008)
FilAng = Subsidiaries.Subsidiaries("RCAT-Angleterre","Angleterre",2014)
newMultinationale.addSubsidiaries(FilTun)
newMultinationale.addSubsidiaries(FilBel)
newMultinationale.addSubsidiaries(FilMar)
newMultinationale.addSubsidiaries(FilAng)

directTuni = Director.Director(10,"VAZ","Yanice",1452,"Tunisie",2017)
FilTun.addSalarie(directTuni)
admiTuni = Administration.Administration(8,"GROLLEAU","Alexis",2014,"Tunisie",2013,60,"Secrétaire")
IngeSeniorTuni = SousEngineer.Senior(7,"RUER","Nathan",1850,"Tunisie",2012,60,80,60,"Programmation")
FilTun.addSalarie(admiTuni)
FilTun.addSalarie(IngeSeniorTuni)

IngeSeniorMaroc = SousEngineer.Senior(7,"GABORIAU","Angele",1450,"Maroc",2013,60,70,90,"Ingé Son")
FilMar.addSalarie(IngeSeniorMaroc)

admiBelg = Administration.Administration(8,"MOCK","Mael",1454,"Belgique",2015,50,"Secrétaire")
IngeJunBelg = SousEngineer.Senior(1,"LEFEBVRE","Eloise",1450,"Belgique",2013,60,70,90,1)
FilBel.addSalarie(admiBelg)
FilBel.addSalarie(IngeJunBelg)


newMultinationale.print()
