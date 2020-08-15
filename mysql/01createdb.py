import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydb")

#If this page is executed with no error, you have successfully created a database.

