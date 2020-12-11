
import mysql.connector

#connection to data base
database = mysql.connector.connect(
    #params necessary
    host = 'localhost',
    user = 'root', #in wampp or xampp
    passwd = '' #we work without password

)

#to check if connection was correct
# print(database) #return <mysql.connector.connection.MySQLConnection object at 0x000001EB5494FBE0>