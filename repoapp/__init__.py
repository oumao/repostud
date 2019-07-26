from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

SUBMITTED_ASSIGNMENT = "/home/ouma/Documents/python/repostud/repoapp/static/submitted_assignments"

app = Flask(__name__)
app.config['SECRET_KEY'] = b'klhohoajoiK09LL81HoljUlOkhla'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:oumaruc2016@localhost/repostud'
app.config['SUBMITTED_ASSIGNMENT'] = SUBMITTED_ASSIGNMENT
app.config['ALLOWED_FILE_EXTENSIONS'] = ['pdf', 'docx', 'txt', 'xlsx', 'pptx']

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "admin_login"
login_manager.login_view = "student_login"
login_manager.login_message_category = "info"

from repoapp import routes