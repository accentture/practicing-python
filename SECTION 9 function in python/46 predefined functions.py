
name = 'Jonathan'

#=======================functions more important

# detect data type
check = isinstance(name, str) # it iwll return if name is str

print(check)
print("================================")

#clear spaces at the beginning and at the end
phrase = '          My name is korah     '
print(phrase)
print(phrase.strip()) #clearing spaces


#eliminate variable 
year = 2020
print(year)
del year #eliminating year variable


#length of variable
text = ' a text'
print(len(text))


#find characters
sentece = 'Life is beatifull'
print(sentece.find('beatiful')) #return the postion where to begin the character


#replace words
newPhrase = 'I am studing python now'
print(newPhrase.replace('now', 'correctly')) #show the new sentence


#uppercase and lowercase words
word = 'JoNaThAn'
print(word.upper())
print(word.lower())
