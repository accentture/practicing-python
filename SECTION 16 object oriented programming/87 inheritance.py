

class Person :
    def __init__(self, name, surname) :
        self.name = name
        self.surname = surname

    def getName(self) :
        return self.name

    def getSurname(self) :
        return self.surname

    def getHigth(self) :
        return self.heigth 

                #applyinng inheritance
class Informatico(Person) :

    # using  constructor of parent
    def __init__(self, name, surname) :
        super().__init__(name, surname)

    def getCompleteName(self) : 
        return self.getName() + ' ' + self.getSurname() #using parent's methods

alejandro = Informatico('jonathan', 'diaz')
print(alejandro.getCompleteName())