
#logical operators 
""" 
    and #y
    or #o
    ! #negation
    not #no 

"""

name = 'Jonathan'
age = 24
country = 'EEUU'

#se lee : si no se cumple esta condicion grande
if not (name == 'Jonathan' and age == 24) :
    print('You are not my master')
else :
    print('wellcome to house master')
print('===========================================================')



if country != 'Perú' and country != 'Bolivia' and country != 'Chile' :
    print('you are not Latinoamerican')
else :
    print('YES. You are Latinoaremican')