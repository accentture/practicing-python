""" 
    --dentro de python biene instalado un sistema gestor de base de datos ligero basado en SQL llamando SQLite
    --este SGBD ya biene instalado dentro del lenguaje
 """

#we will conect to data base

# import module
import sqlite3

""" 
**conecting 
"""
conection = sqlite3.connect('tests.db') #param is name of data base

""" 
**crendo cursor
--permite ejecutar consultas
"""
cursor = conection.cursor()


""" 
**creating table
--con este comando es como se crean todas las consultas sql 
"""
                                        #crea una tabla llamada productos
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
            #en SQLite es obligatorio poner AUTOINCREMENT
            # PRIMARY KEY : para que sea una clave primaria
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+ # la coma debe ir dentro de las comillas siempre
"titulo varchar(255), "+ #tipo caracter de este campo de la columna
"descripcion TEXT, "+ #las claves se pueden poner en minusculas
"precio int(255)"+
")")
#dentro de los parentesis creamos los diferentes campso que va a tener la tabla concatenando strings

""" 
**guardar cambios
--guardaremos cambios que se haya ejecutado aqui
--ahora se ejecutaran las consultas
 """
conection.commit()


#is important to close conection, because but the file stays open and not save changes in this file
conection.close #then a file named tests.db will be created

#finalmente la tabla quedara lista para utilizar




