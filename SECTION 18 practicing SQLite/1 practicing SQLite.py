

#import module to connect to SQLite
import sqlite3

#conecting
conection = sqlite3.connect('programming-topics.db')

#creating cursor to execute queries
cursor = conection.cursor()

#creating table
cursor.execute("CREATE TABLE IF NOT EXISTS topics("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+ 
"topic varchar(255), " +
"description TEXT, " +
"dificulty varchar(255)" +
")")

#inserting data 
cursor.execute("INSERT INTO topics VALUES(null, 'programming fundaments', 'You must learn the most basic programming', 'it is a little difficult')")
cursor.execute("INSERT INTO topics VALUES(null, 'object oriented programming', 'It allows to mantain an aplication', 'it is easy')")
cursor.execute("INSERT INTO topics VALUES(null, 'design patterns', 'It allows to create an scalable and matainable application', 'it is a little difficult')")
cursor.execute("INSERT INTO topics VALUES(null, 'data structures', 'It teachs differents ways to store data, join with asesome algorithms', 'it is very difficult')")

""" #to list data
cursor.execute("SELECT * FROM topics")

print(cursor)



#to show product in a tuple
everyProgramminTopic = cursor.fetchall()
print(everyProgramminTopic)

#iterate every topic
for topic in everyProgramminTopic : 
    print(topic[3]) """



#to get topic of every row
cursor.execute("SELECT topic from topics")
myTopic = cursor.fetchall()
print(myTopic)


#save changes
conection.commit()

#close conection
conection.close()
