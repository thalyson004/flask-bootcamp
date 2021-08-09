# Relationship

import pathlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import backref

basedir = pathlib.Path().absolute() # Get absolute path

app = Flask(__name__) # Set application

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir}\data.sqlite' # Set file location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # No tracking

db = SQLAlchemy(app) # Connect SQLAlchemy DB
Migrate(app, db) # Set Migrate configuration 

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    # One to many (target Model, my Model, load configuration)
    authors = db.relationship('Author', backref='book', lazy='dynamic', uselist=True)

    # One to one (target Model, my Model)
    client = db.relationship('Client', backref='book', uselist=False)   

    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self):
        return f'({self.name}, {self.client}, {self.authors})'

class Author(db.Model):
    __tablename__ = 'authors'
    # Author row has: id (PK), name, book_id (FK)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    book_id = db.Column(db.Integer, db.ForeingKey('books.id'))

    def __init__(self, name, book_id): 
        self.name = name
        self.book_id = book_id

    def __repr__(self) -> str:
        return f'Author: ({self.name}, {self.book_id})'

class Client(db.Model):
    __tablename__ = 'clients'

    # Client row has: id (PK), name, book_id (FK)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    book_id = db.Column(db.Integer, db.ForeingKey('books.id'))

    def __init__(self, name, book_id):
        self.name = name
        self.book_id = book_id 

    def __repr__(self) -> str:
        return f'Client: ({self.name}, {self.book_id})'


