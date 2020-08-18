import mysql.connector


def myconectar():
  try:
    global mydb
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="mydb"
    )
  except Exception as e:
    print("******************************************")
    print("salgo x Error:" + str(e))
    print("******************************************")
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
print("salgo por ok")