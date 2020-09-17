import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mpmp"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydb")

mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE registros (clave VARCHAR(255), valor VARCHAR(255))")
