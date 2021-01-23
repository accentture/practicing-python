""" 
    def __str___ () :
    def __repr___ () :

        --Both __str__ and __repr__ functions return string representation of the object
        --Both of these functions are used in debugging,
        --It’s not a good idea to use these functions directly
        -- if we don’t implement __str__ function then the __repr__ function is called by default in an object
        --You should never use these functions directly and always use str() and repr() functions.
 """

import datetime
now = datetime.datetime.now()
now.__str__()
print(now)

now.__repr__()
print(now)
print('---------------------------------------------')

# example with class
class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def __str__(self): # it is human friendly to read
        return f'Person name is {self.name} and age is {self.age}'

    def __repr__(self): # it contains information about object so that it can be constructed again
        return f'Person(name={self.name}, age={self.age})'


p = Person('Pankaj', 34)

print(p.__str__())
print(p.__repr__())
