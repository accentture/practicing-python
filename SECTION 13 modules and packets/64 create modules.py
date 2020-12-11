
#is import that the name of file is equal to name of import 

""" first way """
#import class_63_introducction_to_modules 

""" second way """
#from class_63_introducction_to_modules import HelloWord
#from class_63_introducction_to_modules import operation

""" third way """
from class_63_introducction_to_modules import * #import all methods, etc

# print(class_63_introducction_to_modules.HelloWord('korah')) #isn't necesary use thus a method imported
print(operation(10, 10))
print(HelloWord('korah'))