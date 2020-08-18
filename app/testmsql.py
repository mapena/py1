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
    print("salgo2 x Excep:" + str(ex))
    print("******************************************")
#  if (mydb):
#    # Carry out normal procedure
#    print ("Connection successful")
#  else:
#    # Terminate
#    print ("Connection unsuccessful")
#    exit()
print("salgo por caida")
exit()
myconectar()
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM registros")
print("********************************")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print("salgo por ok")