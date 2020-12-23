import pathlib
import sys
sys.path.append(str(pathlib.Path().absolute()))


from zRoutes.name import myname ## You can also use '*' wildcard to import all the functions in file.py file.

print(myname.Myname('feo'))