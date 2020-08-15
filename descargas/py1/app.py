def alta():
    return "alta"
def baja():
    return "baja"
def visualizar():
    return "visuzalizar"
def fin():
    return "fin"
def opciones(i):
    switcher = {
        1: alta,
        2: baja,
        3: visualizar,
        4: fin
    }
return switcher.get(i,"Dato invalido")
print ("progamacion en Python")
print ("---------------------")
print (" ")
print ("1) alta registro")
print ("2) bajas registros") 
print ("3) visualizar registros")
#xtexto  = input("ingrese ID :")
#print ("Texto ingresado es : ", xtexto) 

print opciones(1)