from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    return "Hello World"

@app.route('/<name>')
def hello(name):
    return "Hellow {}".format(name)

if __name__=='__main__':
    app.run(debug=True)        