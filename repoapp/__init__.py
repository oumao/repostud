from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate





db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    
    
    from repoapp import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .lecturer import lecturer as lecturer_blueprint
    app.register_blueprint(lecturer_blueprint)

    from .student import student as student_blueprint
    app.register_blueprint(student_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app



    # app.config['SUBMITTED_ASSIGNMENT'] = SUBMITTED_ASSIGNMENT
    # app.config['ALLOWED_FILE_EXTENSIONS'] = ['pdf', 'docx', 'txt', 'xlsx', 'pptx']


# login_manager = LoginManager(app)
# login_manager.login_message = "You must be logged in to access this page."
# login_manager.login_view = "admin_login"
# # login_manager.login_view = "student_login"
# login_manager.login_message_category = "info"

# from repoapp import routes