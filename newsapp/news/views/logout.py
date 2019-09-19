from flask import Blueprint, flash, redirect, url_for, session
from news.views.login_check import is_loggedin

logout_bp = Blueprint('logout_bp', __name__)

@logout_bp.route('/logout')
@is_loggedin
def logout():
	session.clear()
	flash('You have successfully logged out', 'success')
	return redirect(url_for('login_bp.login'))