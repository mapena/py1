import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM registros")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

