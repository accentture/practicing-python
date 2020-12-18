

name = input('Enter yor name: ')
age = int(input('Enter yor age: '))

try :
    if age < 5 or age > 110 :

        #custom error
        raise ValueError ('age entered is not real ')#I can generate differents types of errors with raise keyword
            #indicating what kind of error will throw
    elif len(name) < 1 :

        #custom error
        raise ValueError ("Name entered is not complete  ")
    else : 
        print(f"Wellcome to python Master {name} ")
except ValueError :
    print('Enter your data correctly')
except Exception as err :
    print("It exists an error: ", err)


