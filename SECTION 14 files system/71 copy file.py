import pathlib

# ========================================= to copy file
import shutil


# copy
#to take the file from the current route and copy to other route
mainRoute = str(pathlib.Path().absolute())
print("This is the main route = ", mainRoute)

originalRoute = str(pathlib.Path().absolute()) + '/file-text.txt'
newRoute = str(pathlib.Path().absolute()) + '/copied-file-text.txt'
alternativeRoute = "./SECTION 14 files system/files_copied/other-file-copied.txt"
                   # it is other way to move throw routes, it is different to JS

shutil.copyfile(originalRoute, alternativeRoute)