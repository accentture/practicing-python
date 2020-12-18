""" 
    --working with python file system

    archivo, fichero = file
 """

# to work with file system, we must use the next module
from io import open

#if I want to open the file with an absolute route  then I must import it library
import pathlib

# ================================ open file
#to get the absolute route of this file
                                        #file that I want to create
route = str(pathlib.Path().absolute()) + '/file-text.txt'
print('Mi route absolute = ', route)
file = open(route, "a+") # a+ : the file will be open or created in case if it doesn't exit

# ================================ write between a file
file.write(' ***************** I am a text introduced from python *****************\n')


# ================================ to close file
#always to close a file before to finish
file.close