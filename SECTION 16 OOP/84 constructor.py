
class Car :
    marca = 'toyota'
    color = 'red'

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


#instantiating class
myCar = Car('wolsvage', 'red', 'big')
myCar.showCoche()

myCar2 = Car('Lamgorgini', 'red', 'big')
myCar2.showCoche()