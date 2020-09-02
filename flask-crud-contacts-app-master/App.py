from flask import Flask
from flask import render_template # Archivo index.html
from flask import request  # post
from flask import url_for  # para definir url
from flask import redirect  # para redireccionar la url
from flask import flash  # para mandar mensajes entre vistas
import mysql.connector

app = Flask(__name__)
app.secret_key = "mysecretkey"  # se crea para crear una session que lo utiliza flash para los mensajes.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb"
)
mycursor = mydb.cursor()          
#--------------------------------------------------------------------------------------------------------
# mysql conection 

@app.route('/')   #pagina principal
def Index01():
    sql = "SELECT * FROM registros"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    #print(myresult)
    return render_template('index.html', registros=myresult)

@app.route('/add_reg', methods=['POST'])
def add_reg():
  if request.method == 'POST':
        clave = request.form['clave']
        valor = request.form['valor']
        sql = "INSERT INTO registros (clave, valor) VALUES (%s, %s)"
        val = (clave,valor)
        mycursor.execute(sql, val)
        mydb.commit()
        ###print(mycursor.rowcount, "record inserted.")
        flash(str(mycursor.rowcount) + " Registro/s Agregado/s")
        return redirect(url_for('Index01'))  # se hace refencia a la fun Index que apunta a index.html

@app.route('/delete_reg/<string:id>')    #no hace falta indicar q es un string, se puede colocar id directamente.
def delete_reg(id):
    sql = "DELETE FROM registros WHERE clave like '" + id + "%'"
    #print("sql",sql)
    #mycursor.execute('DELETE FROM registros WHERE clave like {0}',format(id))
    mycursor.execute(sql)
    mydb.commit()
    flash(str(mycursor.rowcount) + " Registro/s Eliminado/s")
    return redirect(url_for('Index01'))  # se hace refencia a la fun Index que apunta a index.html

@app.route('/edit_reg/<id>')   #id recibe un parametro
def get_reg(id):
    sql = "SELECT * FROM registros WHERE clave = '" + id + "'" 
    print("sql=", sql)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(myresult[0])   # myresult[0] significa que me de solo el 1er registro del cursor.
    return render_template('edit-registro.html', registro=myresult[0])

@app.route('/update/<id>', methods=['POST'])
def update_reg(id):
  if request.method == 'POST':
    valor=request.form["valor"]  # request.form["valor"] es tomado del edit-registro.html campo valor
                                 # edit-registro.html por medio del "form action" lo manda a este funcion (update_reg) a # traves de la route('/update/<id>'
    print("id=", id)
    print("valor=", valor)
    mycursor.execute("""
      UPDATE registros 
      SET valor = %s
      WHERE clave = %s
    """,(valor,id))   
    mydb.commit() 
    flash(str(mycursor.rowcount) + " Registro/s Actualizado/s")
  return redirect(url_for('Index01'))


#---------------------------------------------------------------------------------------------------------
# main
#---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(port=3000, debug=True)
