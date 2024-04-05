from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    nombre = input("Cual es tu nombre?")
    return 'hola '+ nombre

@app.route('/login')
def login():
    return("Aquí estara el login")

@app.route('/boyaca')
def boyaca():
    return "Aquí viene Boyaca"

@app.route('/boyaca/aves')
def avesBoy():
    pass

if __name__ == '__main__':
    app.run(debug=True)