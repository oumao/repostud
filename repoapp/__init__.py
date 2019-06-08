from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']=b'klhohoajoiK09LL81HoljUlOkhla'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:oumaruc2016@localhost/repostud'

db = SQLAlchemy(app)


from repoapp import routes
