import pathlib
from collections import defaultdict
from collections import Counter

route = str(pathlib.Path().absolute()) + '/SECTION 0 more about python/python/document.txt'
document = []
with open(route) as f:
  document = f.readlines()
  print(document)


#using built-in methods to sort in python
x = [4, 1, 2, 3]
y = sorted(x) # y is [1, 2, 3, 4], x is unchanged
x.sort() # now x is [1, 2, 3, 4]

print(y)
print(x)

#to sort in a reverse way with the absolute value
                          #key: Based on the results of the key function, you can sort the given list.
                          #abs() function : returns the absolute value of the given number
x = sorted([-4, 1, -2, 3], key=abs, reverse=True) # is [-4, 3, -2, 1]
print(x)

# sort the words and counts from highest count to lowest
print(document)
wc = sorted(document,
key=lambda word_and_count: word_and_count[1], #passsing function to custom sort 
reverse=True)
print(wc)

# sort is finished

