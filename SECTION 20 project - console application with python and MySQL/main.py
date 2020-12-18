""" 
Project with python and MySQL
- Open asistent that ask questions
- login or register
- If we choose register, it will create a user in the database
- If we choose login, it will identify to user
- create notes, display notes or delete notes

 """

# ====================================================== 105 how to make question to assistent

from users import actions
#import users.actions  --- > it is the same that up
#importing my packets

print(""" #inserting quote triple I can insert many prints
Disponible Actions 
    - register
    - login
""")

doThe = actions.Actions() #instantiting class

action = input('¿What do you want to do?: ')

if action == 'register' : 
    doThe.registry()

elif action == 'login' :
    doThe.login()
    

