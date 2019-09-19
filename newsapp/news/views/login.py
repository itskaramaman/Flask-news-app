from flask import render_template, Blueprint, request, flash, redirect, url_for, session
from news.forms import LoginForm
from news.models import User

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST'and form.validate():
		email = request.form['email']
		password_provided = request.form['password']
		result = User.query.filter_by(email=email).first()

		if result != None:
			if result.password == password_provided:
				session['name'] = result.name
				session['logged_in'] = True
				flash('You have succesfully logged in', 'success')
				return redirect(url_for('home_bp.home'))
			else:
				flash('Wrong Credentials', 'danger')
				return redirect(url_for('login_bp.login'))
		else:
			flash('Wrong Credentials', 'danger')
			return redirect(url_for('login_bp.login'))
	return render_template('login.html', form=form)