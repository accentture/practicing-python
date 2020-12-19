# I will create a packet by every model (entities) that I have got (in this case users and notes in database)

#from user import user as model 
import users.user as model # setting an aliase

#importing actions of notes
import notes.actions

class Actions : 

    def registry(self) : #pasing as param the same class
        print('\n Ok, We go to register on the system.')
        names = input('What are your names?: ')
        surnames = input('What are your surnames?: ')
        email = input('What is your email?: ')
        password = input('What is your password?: ')

        user = model.User(names, surnames, email, password)
        print(user.register)
        theRegister = user.register()

        if theRegister[0] >= 1 : 
            print(f"Perfect. {theRegister[1].names} have been registered with email : {theRegister[1].email}")
        else : 
            print("You have not registered correctly.")

    def login(self) :
        try :
            print('\n Ok, We go to register on the system.')
            email = input('What is your email?: ')
            password = input('What is your password?: ')

            user = model.User('','', email, password) # picking only email and password
            login = user.identify()

            if email == login[3] :
                print(f"Wellcome {login[3]} you have been registered in the system the {login[5]}")
                self.proximeActions(login)

        except Exception as e :
            print(type(e))
            print(type(e).__name__)
            print(f"Incorrect login ")

    def proximeActions(self, user) : 
        print("""
        Disponible actions:
            -create note(create)
            -display note(display)
            -eliminate note(eliminate)
            -exit(exit)
        """)

        action = input("you want to do ?: ")
        toDoThe = notes.actions.Actions()
        print(toDoThe)
        if action == 'create' :
            toDoThe.create(user)
            self.proximeActions(user)
        
        elif action == 'display' :
            print("let's display")
            self.proximeActions(user)

        elif action == 'eliminate' :
            print("let's eliminate")
            self.proximeActions(user)

        elif action == 'exit' :
            print(f"Ok {user[1]} let's exit, see you soon!!")
        
        else:
            print("That option isn't exists")


