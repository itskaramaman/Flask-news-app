from flask import render_template, Blueprint
import requests

read_bp = Blueprint('read_bp', __name__)

@read_bp.route('/read-more/<int:index>')
def read(index):
	response = requests.get("https://newsapi.org/v2/everything?q=bitcoin&from=2019-08-16&sortBy=publishedAt&apiKey=10ba003f6d094489a1a07e38a73b7bcd").json()['articles'][index]
	print(response)
	return render_template('read_more.html', response=response)