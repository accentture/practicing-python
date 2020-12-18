
import mysql.connector

database = mysql.connector.connect(
    #params necessary
    host = 'localhost',
    user = 'root',
    passwd = '' ,
    database = 'master_python'
)


cursor = database.cursor(buffered=True) #   buffered = True     :   is is important for that doesn't fail, due sometimes fail by use many times the cursor, it happens when we execute many different queries




#to delete register of the table
#cursor.delete("DELETE FROM vehicules") #it deletes all of registers of the table
cursor.execute("DELETE FROM vehicules WHERE marca = 'Toyota'")
database.commit()

#to check what element of the table was deleted
print(cursor.rowcount, 'deleted')

#to update a register
cursor.execute("UPDATE vehicules SET modelo = 'Aventador' WHERE marca = 'Lamborghini' ")
database.commit()

# to check how many elements were updated
print(cursor.rowcount, 'updated')