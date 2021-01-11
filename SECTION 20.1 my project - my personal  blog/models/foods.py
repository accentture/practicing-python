import pathlib, sys, datetime
sys.path.append(str(pathlib.Path()) + '/SECTION 20.1 my project - my personal  blog' )

import database.connection as conection

database = conection.database
cursor = conection.cursor

class FoodsModel :
    def __init__(self, user_id, category = "", nameOfFood = "", keyword = "") :
        self.user_id = user_id
        self.category = category
        self.nameOfFood = nameOfFood
        self.keyword = keyword
        self.date = datetime.datetime.now()

    def create(self) :
        sql = "INSERT INTO foods VALUES(null, %s, %s, %s, %s)"
        user = (self.user_id, self.category, self.nameOfFood, self.date)

        cursor.execute(sql, user)
        database.commit()

        return cursor.rowcount

    def remove(self) :
        notesWithKeyword = self.__getNotesUsingKeyword()
        numberOfNote = self.__showNotesWithKeyword(notesWithKeyword, 'remove')

        try:
            sql = "DELETE FROM foods WHERE id = %s AND name = %s"
            note = (numberOfNote, self.nameOfFood)
            cursor.execute(sql, note)
            database.commit()

            result = cursor.rowcount

        except Exception as err:
            result = 0
            print("It wasn't possible to remove your note: ", type(err).__name__)

        return result

    def update(self) :
        notesWithKeyword = self.__getNotesUsingKeyword()
        numberOfNote = self.__showNotesWithKeyword(notesWithKeyword, 'update')

        newCategory = input(f"Enter a new category for your note number {numberOfNote} : ")
        newNameFood = input(f"Enter a new name for your food note number {numberOfNote} : ")

        try: 
            sql = "UPDATE foods SET category = %s AND name = %s WHERE id = %s"
            note = (newCategory, newNameFood, numberOfNote)
            cursor.execute(sql, note)
            database.commit()

            result = cursor.rowcount
        except Exception as err :
            result = 0
            print("It wasn't possible to update your note: ", type(err).__name__)

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

     