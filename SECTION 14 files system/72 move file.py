import pathlib

# ========================================= to copy file
import shutil

# to change name
originalRoute = str(pathlib.Path().absolute()) + '/SECTION 14 files system/files_copied/other_file-copied.txt'
toChangeNameRoute = str(pathlib.Path().absolute()) + '/SECTION 14 files system/files_copied/file-with-mame-modified.txt'

shutil.move(originalRoute, toChangeNameRoute)