from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

base_dir =  os.getcwd()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////"+base_dir+"/database/data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "shhhhhh"
db = SQLAlchemy(app)



from news.views import home_bp
app.register_blueprint(home_bp)
from news.views import about_bp
app.register_blueprint(about_bp)
from news.views import read_bp
app.register_blueprint(read_bp)
from news.views import register_bp
app.register_blueprint(register_bp)
from news.views import login_bp
app.register_blueprint(login_bp)
from news.views import logout_bp
app.register_blueprint(logout_bp)
from news.views import main_bp
app.register_blueprint(main_bp)