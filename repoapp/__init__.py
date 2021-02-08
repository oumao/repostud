from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

SUBMITTED_ASSIGNMENT = "/home/ouma/Documents/python/repostud/repoapp/static/submitted_assignments"



def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')




    app.config['SUBMITTED_ASSIGNMENT'] = SUBMITTED_ASSIGNMENT
    app.config['ALLOWED_FILE_EXTENSIONS'] = ['pdf', 'docx', 'txt', 'xlsx', 'pptx']

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

# login_manager = LoginManager(app)
# login_manager.login_message = "You must be logged in to access this page."
# login_manager.login_view = "admin_login"
# # login_manager.login_view = "student_login"
# login_manager.login_message_category = "info"

from repoapp import routes