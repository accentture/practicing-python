import pathlib, sys, datetime, hashlib
sys.path.append(str(pathlib.Path().absolute()) + '/SECTION 20.1 my project - my personal  blog')

#my modules
import database.connection as connection

database = connection.database
cursor = connection.cursor

class User :
    def __init__ (self, names, surnames = "", email = "", password = "") :
        self.names = names
        self.surnames = surnames
        self.email = email
        self.password = password

    def register(self) :
        date = datetime.datetime.now()

        #encode pasword
        _encoded = hashlib.sha256()

        #encoding password
        _encoded.update(self.password.encode('utf8'))

        sql = 'INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)'

        try:
            user = (self.names, self.surnames, self.email, _encoded.hexdigest(), date)
            cursor.execute(sql, user)
            database.commit()

            result = {
                'registerModified':cursor.rowcount,
                'userClass':self
            }
        except Exception as err:
            
            print("An error has ocurred: ", type(err).__name__)

            result = {
                'registerModified':0,
                'userClass':self
            }
        
        return result

    def identify(self) :
        sql = "SELECT * FROM users WHERE names = %s AND password = %s"

        _encoded = hashlib.sha256()  
        _encoded.update(self.password.encode('utf8')) 

        user = (self.names, _encoded.hexdigest())

        try:
            cursor.execute(sql, user)

            result = cursor.fetchone()
            print("getting result", result[4])
        except Exception as err:
            result = 0
            print(type(err).__name__)

        return result

        

#07ed400759a0f606a8b5bfa84712aabe7d1b1c45cb6536c8a5727446b6647b84
#07ed400759a0f606a8b5bfa84712aa