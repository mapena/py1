from flask import Flask,  render_template
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

@app.route('/add_reg')
def add_reg():
         return 'Add registro'

@app.route('/delete_reg')
def delete_reg():
         return 'delete registro'

if __name__ == "__main__":
    app.run(port=3000, debug=True)
