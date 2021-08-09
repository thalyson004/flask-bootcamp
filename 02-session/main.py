from logging import debug
from flask import Flask, request, session
from flask.helpers import url_for
from flask.templating import render_template
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config["SECRET_KEY"] = "mySeCret_KEYy"

class MyForm(FlaskForm):
    username = StringField("Username: ")
    submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def index():
    form = MyForm()
    
    if form.is_submitted():
        session["username"] = form.username.data
        form.username.data=''
        return redirect(url_for('thankyou'))

    return render_template("index.html", form=form)

@app.route("/thankyou")
def thankyou():
    name = "Thalyson gomes Nepomuceno da Silva"
    return f"<h1>Hello {session['username']}</h1>"


if __name__ == "__main__":
    app.run(debug=True)

if __name__=='__main__':
    app.run(debug=True)