
try:
    number = int(input("Number to elevate to square: "))
    print(f"The square number is: {number * number}")
except TypeError : #capturing TypeError
    print("You must to convert your strings to type int")
#except ValueError : #capturing value error
    #print("You must to enter only numbers")

#it serves to display the error in a way more friendly
except Exception as err :   #saving the exception in a variable, if enter to an Exception
    print(type(err)) #it will show type of err = class
    print("An error has ocurred: ", type(err).__name__) # the second param display the type of error

""" VIDEO 77 FINISHED """

