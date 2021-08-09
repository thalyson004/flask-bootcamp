from logging import debug
from flask import Flask, request
from flask.templating import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config["SECRET_KEY"] = "mySeCret_KEYy"

class MyForm(FlaskForm):
    username = StringField("Username: ")
    submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def index():
    username = False
    form = MyForm()
    
    if form.is_submitted():
        username = form.username.data
        form.username.data=''

    return render_template("index.html", username=username, form=form)


if __name__ == "__main__":
    app.run(debug=True)