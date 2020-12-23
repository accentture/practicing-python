
import pathlib, sys
sys.path.append(str(pathlib.Path().absolute()) + '/SECTION 20.1 my project - my personal  blog')
import controllers.actionsUser as controllerUser

print("""
    * Wellcome to personal blog.
    * The next options are disponible:
        - login
        - register
""")

action = input('What do you want to do?: ')

if action == 'login' :
    print("\nOk. Let's enter.")
    user = controllerUser.ActionsUser()
    user.login()

elif action == 'register' : 
    print("\nOk. Let's register.")
    user = controllerUser.ActionsUser()
    user.register()

