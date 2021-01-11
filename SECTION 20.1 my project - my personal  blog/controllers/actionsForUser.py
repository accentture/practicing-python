import pathlib, sys
sys.path.append(str(pathlib.Path().absolute()) + '/SECTION 20.1 my project - my personal  blog')

# model
import models.user as model

#controller
import controllers.actionsForNotes as controllerNotes

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

        names = input("Enter your name: ")
        password = input("Enter your password: ")

        user = model.User(names, "", "", password)
        login = user.identify()

        if names == login[1] :
            print(f"\nWellcome {login[1]} to your personal blog.")
            self.chooseNotes(login[0])
        else :
            print("Login incorrect. Try later.")
    
    def chooseNotes(self, user_id) :
        print("""
            ========== Choose what type of note do you want to create ==========
                - programming 
                - foods 
        """)

        notes = input("Choose your note: ")

        if notes == 'programming' or notes == 'foods':
            controller = controllerNotes.ActionNotes(notes)
            controller.askForActions(user_id)
        else : 
            print("\nThis option doesn't exists.")
       




