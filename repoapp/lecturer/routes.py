from flask import render_template, url_for, session, flash, redirect, request
from flask_login import login_required, login_user, logout_user, current_user
from repoapp import db
from repoapp.lecturer.forms import LecturerRegistrationForm, LecturerLoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from repoapp.models import Lecturer

from . import lecturer

@lecturer.route("/add_lecturer", methods=['POST', 'GET'])
@login_required
def add_lecturer():
    form = LecturerRegistrationForm()

    if form.validate_on_submit():
        hash_pass = generate_password_hash(form.password.data)

        lec = Lecturer(first_name=form.first_name.data, last_name=form.last_name.data, 
                            email=form.email.data, staff_number=form.staff_number.data, password=hash_pass)
        db.session.add(lec)
        db.session.commit()

        flash('Lecturer Successfully Registered', 'success')
        return redirect(url_for('add_lecturer'))

    return render_template("admin/lecturer.html", title="Admin", form=form)

@lecturer.route('/lecturer_login', methods=['GET', 'POST'])
def lecturer_login():
    form = LecturerLoginForm()
    return render_template("lecturer/login.html", title="Lecturer", form=form)

@lecturer.route("/lecturer_table")
@login_required
def lecturer_table():

    lecs = Lecturer.query.all()
    return render_template("admin/lecturer_table.html", title="Admin", lecs=lecs)



