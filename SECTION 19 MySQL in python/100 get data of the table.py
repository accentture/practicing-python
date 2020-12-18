
import mysql.connector

database = mysql.connector.connect(
    #params necessary
    host = 'localhost',
    user = 'root',
    passwd = '' ,
    database = 'master_python'
)


cursor = database.cursor()

""" #cursor.execute('CREATE DATABASE master_python')
cursor.execute('CREATE DATABASE IF NOT EXISTS master_python') #better way 
cursor.execute("SHOW DATABASES")

# ========================== to get all databases
#in the cursor are all data of database
for bd in cursor : 
    print(bd) """


cursor.execute(""" 
CREATE TABLE IF NOT EXISTS vehicules( #it evits to create the same table many times
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,   
    price float(10,2) not null, # entire number can have 10 cifres and decimal numbers can have 2 digits
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)    #this is a restriction
)
""")


#to get data of the table
#cursor.execute("SELECT * FROM vehicules ") #getting all of result of the table
#cursor.execute("SELECT marca FROM vehicules ") #getting only marca

                                        # WHERE : to work as conditional
cursor.execute("SELECT * FROM vehicules WHERE price > 10000 AND marca = 'Lamborghini' ") 

result = cursor.fetchall()

for car in result :
    print(car)


# to get first element of the table
cursor.execute("SELECT * FROM vehicules")
result = cursor.fetchone()
print("Gettin only the first result = ", result)