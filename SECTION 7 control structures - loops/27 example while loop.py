
print('Using while loop')

number = int(input('what number of multiplication number do you want ? :  '))

if number < 1:
    number = 1

counter = 1
while counter <= 10 :
    print(f"{number} x {counter} = {number * counter}")
    counter += 1
else : 
    print('Table finished')