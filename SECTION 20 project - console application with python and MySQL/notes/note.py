# ================================================= this file is a model 
import pathlib
import sys
section20path = str(pathlib.Path().absolute()) + '/SECTION 20 project - console application with python and MySQL'

sys.path.append(section20path)

#importing connection with database
import users.connection as connection
#from users import connection

connect = connection.toConnect()
database = connect[0] #saving database in a variable, it database is in the index 0
cursor = connect[1]

class Note : 

                                    # optional parameters
    def __init__(self, user_id, title = "", description = "") :
        self.user_id = user_id
        self.title = title
        self.description = description
        
    # to save in database
    def save(self) :
                                                        # NOW() : sql function, it allows save date automatically
        sql = "INSERT INTO notes VALUES(null, %s, %s, %s, NOW())"
        note =(self.user_id, self.title, self.description)

        cursor.execute(sql, note)
        database.commit()

        return [cursor.rowcount, self] # rowcount : return rows that were inserted


    #this method to get notes from database
    def toList(self) :
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"
        cursor.execute(sql)

        result = cursor.fetchall()

        return result

    def remove(self) :
                                                                            # %{title}% : checking if title exists
                                                                            # cuando el titulo esté contenido dentro del título que este guardado
        sql = f"DELETE FROM notes WHERE user_id = {self.user_id} AND title LIKE '%{self.title}%' "

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self] #cursor.rowcount : amount of rows affected
