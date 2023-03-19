""" 
SET : es un tipo de dato, para tener una coleccion de valores, pero no tiene indice ni orden
 """

#in a set there aren't order
#a set has not repeated elements 
people = {
    'juan',
    'pedro',
    'javier'
}
people.add('paco')
people.add('pedro')
people.remove('javier')
print(type(people))

print(people)