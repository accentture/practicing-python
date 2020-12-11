

numbers = [45,23,5,12,64,6]
programmingLanguages = list(('java','php','javascript','C','php', 'php')) 

#sort numbers
numbers.sort()
print(numbers)
programmingLanguages.append('c#')
programmingLanguages.insert(7, 'scala') #the first param is the position
print(programmingLanguages)


#elimnate an element
numbers.pop(2) #poram is the index
programmingLanguages.remove('php')
print(numbers)

#invert an array
numbers.reverse()

#search an element in an array
print('javascript' in programmingLanguages) #return True

#count element
print(len(programmingLanguages))

#how many times appears an element
print(programmingLanguages.count('php'), 'times' )

#to get index of an element
print(programmingLanguages.index('java'))

#to join list
programmingLanguages.extend(numbers)
print(programmingLanguages)