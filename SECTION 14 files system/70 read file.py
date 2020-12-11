

from io import open


import pathlib

                                        # this is the file name
route = str(pathlib.Path().absolute()) + '/file-text.txt'
print('Mi route absolute = ', route)
file = open(route, "a+") 

# ================================ write between a file
#file.write(' ***************** I am a text introduced from python *****************\n')


# ================================ read file
route = str(pathlib.Path().absolute()) + '/file-text.txt'
fileToRead = open(route, "r")  # r : a different permission (to read file) 

#to read
""" content = fileToRead.read()
print(content) """

# read every line of "file-text.txt"the content and save in a list 
list = fileToRead.readlines()

fileToRead.close()

for phrase in list : 

    phraseInArray = phrase.split()
    print(phraseInArray)
    print(' -- text centered - ', phrase.center(100)) #to center the list with 100 spaces