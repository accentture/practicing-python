
class Car :

    #public properties by default
    marca = 'toyota'
    color = 'red'

    #setting private property using sub script
    __tires = 'the most bigger'

    def __init__(self, marca, color, size) :   
        self.marca = marca
        self.color = color
        self.size = size
    
    def showCoche(self) : 
        print(self.marca)

    #using getter and setter
    def getMarca(self) :
        return self.marca

    def setMarca(self, marca) :
        self.marca = marca

    def getPrivate(self) :
        return self.__tires




myCar = Car('wolsvage', 'red', 'big')
myCar.showCoche()

#print(myCar.__tires) #throw attribute error
print(myCar.getPrivate()) #getting private property with getter

""" VIDEO 87 FINISHED """

