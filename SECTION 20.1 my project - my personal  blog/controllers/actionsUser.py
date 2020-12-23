import pathlib, sys
sys.path.append(str(pathlib.Path().absolute()) + '/SECTION 20.1 my project - my personal  blog')

import models.user as model

class ActionsUser : 
    def register(self) :
        print(" ============= Enter your data =============")

        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        user = model.User(name, surname, email, password)

        user.register()

    def login(self) :
        print(" ============= Enter your data =============")

        name = input("Enter your name: ")
        password = input("Enter your password: ")

        user = model.User(name, password)

        print(user)