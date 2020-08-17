from flask import Flask, 
from flask import render_template, # Archivo index.html
from flask import request  # post
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydb"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/')
def Index():
     return render_template('index.html')

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
        print(mycursor.rowcount, "record inserted.")
        ###cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
        ###mysql.connection.commit()
        ###flash('Contact Added successfully')
        ###return redirect(url_for('Index'))   
        
        return "metodo add"

@app.route('/delete_reg')
def delete_reg():
         return 'delete registro2'

if __name__ == "__main__":
    app.run(port=3000, debug=True)
