import pathlib, sys, datetime
sys.path.append(str(pathlib.Path()) + '/SECTION 20.1 my project - my personal  blog')
import database.connection as connection

database = connection.database
cursor = connection.cursor

class ProgrammingModel :
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
        notesWithKeyword = self.__getNotesUsingKeyword()
        numberOfNote = self.__showNotesWithKeyword(notesWithKeyword, 'remove')

        try:
            date = datetime.datetime.now()
            sql = "DELETE FROM programming WHERE id = %s AND topic = %s"
            note = (numberOfNote, self.topic)

            cursor.execute(sql, note)
            database.commit()

            result = cursor.rowcount
        except Exception as err:
            result = 0
            print() 

        return result

    def update(self) :
        notesWithKeyword = self.__getNotesUsingKeyword()
        numberOfNote = self.__showNotesWithKeyword(notesWithKeyword, 'update')

        newDescription = input(f"Enter a new description for your note number {numberOfNote} : ")
        date = datetime.datetime.now()
        
        try : 
            sql = "UPDATE programming SET description = %s AND _date = %s WHERE id = %s"
            note = (newDescription, date, numberOfNote) 
            print("Note to update => ", note)
            cursor.execute(sql, note)
            database.commit()

            result = cursor.rowcount

        except Exception as err :
            result = 0
            print("An error has ocurred trying to update", type(err).__name__)

        return result

    def __getNotesUsingKeyword(self) :
        sql = "SELECT * FROM programming"
        cursor.execute(sql)
        result = cursor.fetchall()

        notesWithKeyword = [] #to show to user

        for note in result :
            if self.keyword in note[3] :
                notesWithKeyword.append(note)
            
        return notesWithKeyword

    def __showNotesWithKeyword(self, notes, query) :

        print("\n=========== The next notes have your keyword:")
        for note in notes : 
            print(note)

        print(f"\nChoose the first position of the tuple. It allows to {query} your note.")

        position = input("Write a number: ")

        return position

    
            

    



        
