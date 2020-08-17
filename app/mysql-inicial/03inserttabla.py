import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO registros (clave, valor) VALUES (%s, %s)"
val = ("clave3", "valor3")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

