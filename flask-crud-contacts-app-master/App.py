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
    print(myresult)
    return render_template('index.html', registros=myresult)

@app.route('/add_reg', methods=['POST'])
def add_reg():
  if request.method == 'POST':
        clave = request.form['clave']
        valor = request.form['valor']
        #print("clave", clave)
        #print("valor", valor)
        sql = "INSERT INTO registros (clave, valor) VALUES (%s, %s)"
        val = (clave,valor)
        mycursor.execute(sql, val)
        mydb.commit()
        ###print(mycursor.rowcount, "record inserted.")
        ###cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
        ###mysql.connection.commit()
        ###flash('Contact Added successfully')
        ###return redirect(url_for('Index'))   
        flash('Registro Agregado')
        return redirect(url_for('Index'))  # se hace refencia a la fun Index que apunta a index.html

@app.route('/delete_reg/<string:id>')
def delete_reg(id):
    print(id)
    return id

if __name__ == "__main__":
    app.run(port=3000, debug=True)
