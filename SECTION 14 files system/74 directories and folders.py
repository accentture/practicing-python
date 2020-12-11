
import os, shutil

# always it is recommendable to use a absolute route
currentDirectory = os.path.abspath("./")
print("Mi absolute path = ", currentDirectory)

# ========================= creating a folder
if not os.path.isdir('./SECTION 14 files system/folder_created_with_python') : 
    
    #mkdir : it allows to create a folder
    os.mkdir("./SECTION 14 files system/folder_created_with_python")
else :
    print("This directory already exist")


# ====eliminate a folder
#os.rmdir('./SECTION 14 files system/folder_created_with_python')


# ==== copy folder

""" originalRoute = './SECTION 14 files system/folder_created_with_python'
newRoute = './SECTION 14 files system/folder_created_with_python_copied'
shutil.copytree(originalRoute, newRoute) #eliminate folder """


# ==== to list content of folder
content = os.listdir('./SECTION 14 files system/folder_created_with_python')
print("Mi files from folder_created_with_python folder = ", content)

""" VIDEO 74 FINISHED """