from flask import render_template, Blueprint
import requests
from news.views.login_check import is_loggedin

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
@is_loggedin
def home():
	response = requests.get("https://newsapi.org/v2/everything?q=bitcoin&from=2019-08-16&sortBy=publishedAt&apiKey=10ba003f6d094489a1a07e38a73b7bcd").json()
	return render_template('home.html', response=response)