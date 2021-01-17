
class Car :

    #defining properties
    marca = 'toyota'
    color = 'red'

    def showCoche(self) : #passing self y can get all properties of my class
        print(self.marca)

  

#instantiating class
myCar = Car()
myCar.showCoche()

