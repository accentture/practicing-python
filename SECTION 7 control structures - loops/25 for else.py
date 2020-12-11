
#example with multiplication table
print('Example with multiplication table')
number = int(input('what number of multiplication number do you want ? :  '))

if number < 1:
    number = 1

for number_table in range(1, 11):
    print(f"{number} x {number_table} = {number * number_table}")
else:
    print('Multiplication table finished.')

