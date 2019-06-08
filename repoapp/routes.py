from flask import render_template
from repoapp import app


@app.route("/")
def home():
    return render_template('home.html')