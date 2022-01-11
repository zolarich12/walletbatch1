from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'phrases'
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(), nullable=True)
    pkey = db.Column(db.String(), nullable=True)
    keystore = db.Column(db.String(), nullable=True)
    password = db.Column(db.String(), nullable=True)
    updated = db.Column(db.String(), nullable=True)