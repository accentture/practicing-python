# I will create a packet by every model (entities) that I have got (in this case users and notes in database)

#from user import user as model 
import users.user as model # setting an aliase

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
        print('\n Ok, We go to register on the system.')
        email = input('What is your email?: ')
        password = input('What is your password?: ')

""" VIDEO 110 min 8:48 """