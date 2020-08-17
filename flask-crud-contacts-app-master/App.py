from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
     return "Hola Marce3"

@app.route('/add_contact')
def add_contact():
         return 'Add contacto'

if __name__ == "__main__":
    app.run(port=3000, debug=True)
