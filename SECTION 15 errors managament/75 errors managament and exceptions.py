""" 
    --code susceptible to errors
 """

#how to capture exceptions and to manganament errors in fails susceptible code or erros

""" it is as try cath in JavaScript """
# use try except if we believe that some code can give whatever error
try:
    name = input('What is your name: ')

    #exeption using local variable
    if len(name) > 1 :
        user_name = f"the name is {name}"

    print(user_name)
except:
    print("An error has ocurred, enter good your name...")
else:
    print("Everything has worked perfectly")
finally:
    print('end of iteration!!' ) #it allays will be executed
