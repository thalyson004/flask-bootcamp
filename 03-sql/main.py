import pathlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # For migrate (change database)

path = pathlib.Path().absolute()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{path}\data.sqlite'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) # Connect db to app
Migrate(app, db) # Given migrate capability do migrate
 
###############################

class User(db.Model):
    
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    year = db.Column(db.Integer)
    heigth = db.Column(db.Integer)

    def __init__(self, name, year, height):
        self.name = name
        self.year = year
        self.height = height

    def __repr__(self):
        return f"Name: {self.name}, year: {self.year}, height: {self.heigth} ({self.id})"

if __name__=='__main__':
    print( path )