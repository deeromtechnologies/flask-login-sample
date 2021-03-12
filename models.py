import os
from sqla_wrapper import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///db.sqlite"))  # this connects to a database either on Heroku or on localhost




class User(UserMixin,db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	name = db.Column(db.String(80), unique=False, nullable=False)
	gender = db.Column(db.String(80), unique=False, nullable=False)
	address = db.Column(db.String(200), unique=False, nullable=False)
	contact = db.Column(db.String(80), unique=False, nullable=False)
	password = db.Column(db.String(80), unique=False, nullable=False)
	def __init__(self, email,password, name, address, gender, contact):
		
		self.name = name
		self.gender = gender
		self.address=address
		self.email=email
		self.contact = contact
		self.password = password
	