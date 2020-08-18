import mysql.connector



try:
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydbx"
  )

except:
  if (mydb):
    # Carry out normal procedure
    print ("Connection successful")
  else:
    # Terminate
    print ("Connection unsuccessful")
    exit()

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM registros")
print("********************************")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
