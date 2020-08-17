from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
     return "Hola Marce3"

@app.route('/add_reg')
def add_contact():
         return 'Add registro'

@app.route('/delete_reg')
def add_contact():
         return 'delete registro'

if __name__ == "__main__":
    app.run(port=3000, debug=True)
