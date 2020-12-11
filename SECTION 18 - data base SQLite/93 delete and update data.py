

import sqlite3

""" 
**conecting 
"""
conection = sqlite3.connect('tests.db') 

""" 
**crendo cursor
--permite ejecutar consultas
"""
cursor = conection.cursor()


""" 
**creating table
--con este comando es como se crean todas las consultas sql 
"""

#other way to                    
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    titulo varchar(255), 
    descripcion TEXT, 
    precio int(255)
);
""")

""" 
**guardar cambios

 """
conection.commit()



""" insert data """
""" 
cursor.execute("INSERT INTO productos VALUES(null, 'primer producto', 'descripcion de mi producto', 550 )") #elegimos los valores que queremos meter dentro de los parentesis
conection.commit()#save changes y execute the query, insterting this new product in the table
 """

""" delete registers """
#cursor.execute("DELETE FROM productos") #delelte all productos of the table
#conection.commit() #this code is important to every action over data base

""" insert many registers  """
newProducts = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono movil", "Buen telefono", 140),
    ("Placa base", "Buena placa", 80),
    ("tablet 15" , "Buena tablet", 300)
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", newProducts) #passing as param newProducts
conection.commit() #to do to work it use this code

""" to upadate data """
#modificaremos precio al producto que tenga como precio = 80
cursor.execute("UPDATE productos SET precio=1000 WHERE precio = 80")

""" to list data """
                                    #we can use condionals
cursor.execute("SELECT * FROM productos WHERE precio >= 300;") # the asterisc is to select all columns of the table

#to see  what are between my query
print(cursor) #retrun an object between the cursor : Cursor object at 0x0000024E501E3960

#to show the products
productos = cursor.fetchall()
print(productos) #every product is in a tuple




#we can access to every product
for product in productos : 
    print("ID: ", product[0]) #to see the incremental
    print(product)
    print(product[1]) #acceding the field of the table
    print("\n")

#to get the first title of the table
cursor.execute("SELECT titulo FROM productos") 
otherProduct = cursor.fetchone()
print(otherProduct)

#is important to close conection, because but the file stays open and not save changes in this file
conection.close #then a file named tests.db will be created


#finalmente la tabla quedara lista para utilizar




