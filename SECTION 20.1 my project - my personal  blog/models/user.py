import pathlib, sys, datetime, hashlib
sys.path.append(str(pathlib.Path().absolute()) + '/SECTION 20.1 my project - my personal  blog')

#my modules
import database.connection as connection

connect = connection.toConnect()
database = connect['database']
cursor = connect['cursor']

class User :
    def __init__ (self, names, surnames, email, password) :
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

        user = (self.names, self.surnames, self.email, _encoded.hexdigest(), date)
        cursor.execute(sql, user)
        database.commit()

        result = {
            'registerModified':cursor.rowcount,
            'userClass':self
        }
        
        return result

    #def identify(self) :
        
