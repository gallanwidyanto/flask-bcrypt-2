from app import bcrypt
from database import db


class UserModel(db.Model):
	
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(45))
	password = db.Column(db.String(70))

	def __init__(self, username, password):
		self.username = username
		self.password = password)