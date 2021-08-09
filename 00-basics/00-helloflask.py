from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'

@app.route('/info')
def info():
    return '<h1>Info!</h1>'

@app.route('/user/<name>')
def user(name):
    name = str(name)
    if name.endswith('y'):
        name = name[:-1]+'iful'
    else:
        name = name+'y'
        
    return f'<h1>My name is {name}</h1>'

if __name__ == "__main__":
    app.run()