
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


cursor.execute("SHOW TABLES")

for table in cursor : 
    print(table)

""" 
#to insert data in a table
cursor.execute("INSERT INTO vehicules VALUES(null, 'Opel', 'Astra', 18500)")

#it is important to execute the commit, because then it don't save the query
#the database is who has the commit but don't cursor
database.commit()
 """

#inserting data masively
cars = [
    ('Seat', 'Ibiza', 5000),
    ('Lamborghini', 'Huracan', 50000),
    ('Toyota', 'las narices', 10000), #it is important doesn't insert space between a data 'Toyota  ' for example
    ('Bugatti Veiron', 'la de CR7', 1000000),
]

#inserting many cars to the table
                                                    # %s allows to substitute by other data
cursor.executemany("INSERT INTO vehicules VALUES(null, %s, %s, %s)", cars)
database.commit()