from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
