import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE registros (clave VARCHAR(255), valor VARCHAR(255))")

#If this page is executed with no error, you have successfully created a table named "customers".

