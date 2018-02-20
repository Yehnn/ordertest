from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Product(db.Model):
    __tablename__='product'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    quantity=db.Column(db.Integer)
    price=db.Column(db.Integer)


class User(db.Model):
    __tablename__='user'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    money=db.Column(db.Integer)
