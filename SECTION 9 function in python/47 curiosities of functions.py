

#always to define the functions at the beginning of the file
def myFirstFucntion() :
    return 'How are you ' + nameGlobal  #always a function must return a value

def mySecondFucntion() :
    return 'How are you 2 ' + nameGlobal

#to define global variables after the functions
nameGlobal = 'Jonathan'

#recomendable always to pass params to functions
print(myFirstFucntion())
print(mySecondFucntion())