import mysql.connector
mydb = 0
def myconectar():
  try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="mydb"
   )
  except:
    print("Error de conexcion")
    exit()
#  if (mydb):
#    # Carry out normal procedure
#    print ("Connection successful")
#  else:
#    # Terminate
#    print ("Connection unsuccessful")
#    exit()

myconectar()
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM registros")
print("********************************")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
