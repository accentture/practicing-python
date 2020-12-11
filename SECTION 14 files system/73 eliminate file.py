import pathlib

# ===================== module to eliminate files
import os

toChangeNameRoute = str(pathlib.Path().absolute()) + '/SECTION 14 files system/files_copied/file-with-mame-modified.txt'

# eliminate file
#os.remove(toChangeNameRoute)

#=============================== to check if a file exist
import os.path
                                            # ./  : current directory
print("Mi absolute path = ", os.path.abspath("./")) # return the absolute path

currentDirectory = os.path.abspath("./")

if os.path.isfile(currentDirectory + '/file-text.txt') :
    print('The file exist')
else :
    print("The file doesn't exit")
