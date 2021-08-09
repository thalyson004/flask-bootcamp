from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index-ex.html")

@app.route('/report')
def report():
    username = request.args.get('username')
    print( hasLowercase(username) )
    print( hasUppercase(username) )
    print( endsWithNumber(username) )
    return render_template("report-ex.html", username=username)

def hasLowercase(name):
    for letter in name:
        if letter.islower():
            return True

    return False

def hasUppercase(name):
    for letter in name:
        if letter.isupper():
            return True

    return False

def endsWithNumber(name):
    return name[-1].isnumeric()

if __name__ == "__main__":
    app.run(debug=True)

