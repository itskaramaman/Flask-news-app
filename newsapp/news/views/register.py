from flask import render_template, Blueprint, request, session, redirect, url_for, flash
from news.forms import RegisterationForm
from news.models import User
from news import db

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterationForm(request.form)
	if request.method == 'POST' and form.validate():
		name = request.form['name']
		email = request.form['email']
		username = request.form['username']
		password = request.form['password']
		new_user = User(name, email, username, password)
		db.session.add(new_user)
		db.session.commit()
		flash('You have been registered successfully', 'success')
		return redirect(url_for('home_bp.home'))
	return render_template('register.html', form=form)