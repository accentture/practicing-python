""" this file is a model """

#importing connection with database
import users.connection as connection

connect = connection.toConnect()
database = connect[0] #saving database in a variable, it database is in the index 0
cursor = connect[1]

class Note : 

    def __init__(self, user_id, title, description) :
        self.user_id = user_id
        self.title = title
        seff.description = description

    # to save in database
    def save(self) :
                                                        # NOW() : sql function, it allows save date automatically
        sql = "INSERT INTO notes VALUES(null, %s, %s, %s, NOW())"
        note =(self.user_id, self.title, self.description)

        cursor.execute(sql, note)
        database.commit()

        return [cursor.rowcount, self] # rowcount : return rows that were inserted


