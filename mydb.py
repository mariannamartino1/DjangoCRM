import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Inserisci22!'

)

#prepare cursor object
cursorObject = dataBase.cursor()

#Create DataBase
cursorObject.execute("CREATE DATABASE elderco")

