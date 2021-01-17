
class Car :

   
    marca = 'toyota'
    color = 'red'

    def showCoche(self) : 
        print(self.marca)

    #using getter and setter
    def getMarca(self) :
        return self.marca

    def setMarca(self, marca) :
        self.marca = marca


#instantiating class
myCar = Car()
myCar.showCoche()

myCar.setMarca('Buggaty Veiron') 
print(myCar.getMarca())