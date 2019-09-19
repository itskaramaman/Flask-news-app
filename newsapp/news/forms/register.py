from wtforms import Form, StringField, PasswordField, validators

class RegisterationForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=100)])
	email = StringField('Email', [validators.Length(min=1, max=100)])
	username = StringField('Username', [validators.Length(min=1, max=30)])
	password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message="Password didn't matched")])
	confirm = PasswordField('Confirm Password', [validators.Length(min=1)])
	