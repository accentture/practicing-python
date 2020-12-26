import pathlib, sys, datetime
sys.path.append(str(pathlib.Path()) + '/SECTION 20.1 my project - my personal  blog')
import database.connection as connection

database = connection.database
cursor = connection.cursor

class ProgrammingNote :
    def __init__(self, user_id, topic, description = "", keyword = "") :
        self.user_id = user_id
        self.topic = topic
        self.description = description
        self.keyword = keyword

    def create(self) :
        date = datetime.datetime.now()
        sql = "INSERT INTO programming VALUES(null, %s, %s, %s, %s)"
        user = (self.user_id, self.topic, self.description, date)

        cursor.execute(sql, user)
        database.commit()

        result = {
            'registerModified':cursor.rowcount,
            'classNote': self
        }
        print(result['registerModified'])

        return result
    def remove(self) :
        notesWithKeyword = self.getNotesUsingKeyword()

        date = datetime.datetime.now()
        sql = "DELETE FROM programming WHERE "
        user = ""

    def update(self) :
        date = datetime.datetime.now()

    def getNotesUsingKeyword(self) :
        sql = "SELECT * FROM programming"
        cursor.execute(sql)
        result = cursor.fetchall()

        notesWithKeyword = []

        for note in result :
            if self.keyword in note[3] :
                notesWithKeyword.appen(note)
            
        return notesWithKeyword

    



        
