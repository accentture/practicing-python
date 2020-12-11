
#global variable
message = 'My dog is awesome'
print(message)

def showMessage() :
    #local variable
    #message = 'My chicken is strong'

    print(message)

    global year #converting to global variable, but only after to execute showMessage() function
    year = 4040
    print(year)
showMessage()

#it isn't posible to acces to year variable outside of the function
print(year)
