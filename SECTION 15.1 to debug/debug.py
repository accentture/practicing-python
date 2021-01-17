
def substration( num2, num3) : 
    return num1 - num2

def adition(num1, num2) :
    return num1 + num2 

def operationCombinated(num1, num2, num3) :

    breakpoint() # breakpoint allows to debug
                 # it is possible to use many breakpoints

    """ 
        -- to know what line is the code, where it line haven't excecuted yet : l
        -- to continue with the next line of code : n
        -- to continue with the next line, but it line has a function and we want to check it : s
        -- to jump lines : j 23   ;  where 23 is line that I want to jump
        -- to end execution : c
        -- to jump between breakpoints : c
        -- to check argumets in the funcion : a

        -- to check help : h
        -- to check help depply; for example : h j

    """ 

    otherNumber = 234  # it is possible to modfiy whatever value in the next way :  otherNumber = 55555

    _adition =  adition(num1, num2)
    _substraction = substration(_adition, num3)

    return _substraction

print(operationCombinated(10, 96, 6))