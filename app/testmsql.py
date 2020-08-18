import mysql.connector


def myconectar():
  try:
    global mydb
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="mydbx"
    )
  except Exception as er:
    print("******************************************")
    print("salgo2 x Excep:" + str(er))
    print("******************************************")
#  if (mydb):
#    # Carry out normal procedure
#    print ("Connection successful")
#  else:
#    # Terminate
#    print ("Connection unsuccessful")
#    exit()
myconectar()

print("salgo por caida")
exit()

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM registros")
print("********************************")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print("salgo por ok")