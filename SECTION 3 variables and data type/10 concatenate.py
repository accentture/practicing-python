
name = 'Jonathan'
surname = 'Díaz'
age = '28'

#concating
#only can concat strings
print(name + ' ' + surname + ' has ' + age + ' years.')

#using interpolation
print(f"{name} {surname} has {age} years")

#using format() method
print("Hi mi name is {} {} and have {} years.".format(name, surname, age))
                                            #passing parameters to format() method

#it will concat automatically
print(name, surname, age)