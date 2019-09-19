from news import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False)
	username = db.Column(db.String(30), unique=True, nullable=False)
	password = db.Column(db.String(100), nullable=False)

	def __init__(self, name, email, username, password):
		self.name = name
		self.email = email
		self.username = username
		self.password = password

	def __repr__(self):
		return "<User(id=%s, name='%s', email='%s', username='%s, password='%s')>" % (
            self.id, self.name, self.email, self.username, self.password)