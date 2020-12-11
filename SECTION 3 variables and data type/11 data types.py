
#main data type  
nothing = None #type None
string = 'Ugly'
entireNumber = 44
flotant = 3.3
boolean = True #this value begin with uppercase
lista = [3,4,5,6,67,7]
tupla = ('my', 'name', 'is', 'Jonathan') #a tupla is a lis of data that cannot change, it is equal to a list

#it is as a json document in JS
dictionary = {
    'name':'Jonathan',
    'surname':'Díaz',
    'age':24
}
rangeValue = range(9) #type range
date_byte = b"Probando" #with a fowrdward, it becomes a type byte date

print(nothing)
print(boolean)
print(lista)
print(tupla)
print(dictionary)
print(rangeValue)
print(date_byte)

#to print data type
print('-----------------------------------------------------------------')
print(type(nothing))
print(type(string))
print(type(entireNumber))
print(type(flotant))
print(type(lista))
print(type(tupla))
print(type(dictionary))
print(type(rangeValue))
print(type(date_byte)) 

