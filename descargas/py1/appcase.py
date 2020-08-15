import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydb"
)
mycursor = mydb.cursor()


def alta():
    dato  = input("ingrese registro :")
    print("reg:",dato)
    sql = "INSERT INTO registros (clave, valor) VALUES (%s, %s)"
    val = (dato, dato)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return 
def baja():
    dato  = input("ingrese registro :")
    print("reg:",dato)
    sql = "DELETE FROM registros WHERE clave = %dato "
    sql = "INSERT INTO registros (clave, valor) VALUES (%s, %s)"
    val = (dato, dato)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return 
def visualizar():
    return 'visu'

def opciones(i):
    switcher = {
            1: alta,
            2: baja,
            3: visualizar,
            4: lambda: exit()
            }
    func = switcher.get(i, lambda: 'Invalid')
    return func()

print ("progamacion en Python")
print ("---------------------")

print (" ")
print ("1) alta registro")
print ("2) bajas registros") 
print ("3) visualizar registros")
print ("4) fin")
idopcion = 9
while idopcion != 4:
    idopcion  = int(input("ingrese numero :"))
    print ("Texto ingresado es : ", idopcion)
    print (opciones(idopcion))
    print ("while ..")
    
print("salgo while")