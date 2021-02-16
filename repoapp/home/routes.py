from flask import render_template
from . import home


@home.route("/")
@home.route("/home")
def home():
    return render_template('home.html', title="Home")
