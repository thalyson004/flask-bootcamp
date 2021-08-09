from os import name
from re import template
from flask import Flask
from flask import request
from flask.templating import render_template
from flask.wrappers import Request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup_form')
def signup_form():
    return render_template("signup.html")

@app.route('/thanks')
def thank_you():
    first = request.args.get('first') 
    last = request.args.get('last')
    return render_template("thanks.html", first=first, last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("page_not_found.html"), 404 

if __name__ == "__main__":
    app.run(debug=True)