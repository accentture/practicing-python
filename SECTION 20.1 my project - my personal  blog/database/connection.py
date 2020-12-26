import mysql.connector

def toConnect() :
    database = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'personal_blog',
        port = '3306'
    )

    cursor = database.cursor(buffered = True)

    return {
        'database':database,
        'cursor':cursor
    }

connection = toConnect()
database = connection['database']
cursor = connection['cursor']