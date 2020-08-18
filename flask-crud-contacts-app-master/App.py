from flask import Flask
from flask import render_template # Archivo index.html
from flask import request  # post
from flask import url_for  # para definir url
from flask import redirect  # para redireccionar la url
from flask import flash  # para mandar mensajes entre vistas
import mysql.connector

# mysql conection 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydb"
)
mycursor = mydb.cursor()
app = Flask(__name__)

app.secret_key = "mysecretkey"  # se crea para crear una session que lo utiliza flash para los mensajes.
@app.route('/')   #pagina principal
def Index():
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
        return redirect(url_for('Index'))  # se hace refencia a la fun Index que apunta a index.html

@app.route('/delete_reg/<string:id>')    #no hace falta indicar q es un string, se puede colocar id directamente.
def delete_reg(id):
    sql = "DELETE FROM registros WHERE clave like '" + id + "%'"
    #print("sql",sql)
    #mycursor.execute('DELETE FROM registros WHERE clave like {0}',format(id))
    mycursor.execute(sql)
    mydb.commit()
    flash(str(mycursor.rowcount) + " Registro/s Eliminado/s")
    return redirect(url_for('Index'))  # se hace refencia a la fun Index que apunta a index.html

@app.route('/edit_reg/<id>')   #id recibe un parametro
def get_reg(id):
    mycursor.execute("SELECT * FROM registros WHERE clave = %s",(id))
    myresult = mycursor.fetchall()
    print(myresult)
    return "fun edit_reg" 

if __name__ == "__main__":
    app.run(port=3000, debug=True)
