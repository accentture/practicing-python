#connecting to database
import mysql.connector

def toConnect() :
    database = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'master_python',
        port = 3306 #port : it is the port by where to work the database
    )
    #if I want to create a user , I can go user account in phpMyAdmin

    #cursor to query
    cursor = database.cursor(buffered = True) # buffered = True : it allows to do many queries using the same cursor

    return [database, cursor]