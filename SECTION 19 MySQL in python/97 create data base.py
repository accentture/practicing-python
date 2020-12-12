
import mysql.connector

#connection to data base


database = mysql.connector.connect(
    #params necessary
    host = 'localhost',

                #write root also in phpMyAdmin
    user = 'root', #in wampp or xampp, unless that I create an MySQL user join to a password, it is done in phpMyAdmin
    passwd = '', #we work without password
    database = 'master_python'# AFTERR to create database, I can pass this param
               # it make a us of database in order to make queries to database
)

# ========================== to check if connection was correct
# print(database) #return <mysql.connector.connection.MySQLConnection object at 0x000001EB5494FBE0>

# ========================== queries with MySQL cursor
cursor = database.cursor()

# ==========================creating database
#cursor.execute('CREATE DATABASE master_python')
cursor.execute('CREATE DATABASE IF NOT EXISTS master_python') #better way 

# ========================== to ckeck if a database exist
# first - to check in phpMyAdmin and search master_python database
# second - is code of low
cursor.execute("SHOW DATABASES")

# ========================== to get all databases
#in the cursor are all data of database
for bd in cursor : 
    print(bd)