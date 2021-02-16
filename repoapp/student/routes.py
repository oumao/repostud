
from flask import render_template, url_for, session, flash, redirect, request
from flask_login import login_required, login_user, logout_user, current_user
from repoapp import db
from repoapp.student.forms import StudentRegistrationForm, StudentLoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from repoapp.models import Student

from . import student

""" Student Routes """

@student.route("/add_student", methods=['POST', 'GET'])
@login_required
def add_student():
    
    form = StudentRegistrationForm()

    if form.validate_on_submit():
        hash_pass = generate_password_hash(form.password.data)
        student = Student(first_name=form.first_name.data, last_name=form.last_name.data, 
                        admission_number=form.admission_number.data, birth_date=form.birth_date.data, gender=form.gender.data, 
                        program=form.program.data, study_year=form.study_year.data, password=hash_pass )

        db.session.add(student)
        db.session.commit()
        flash('Student successfully registered!', 'success')
        return redirect(url_for('add_student'))
    return render_template("admin/student.html", title="Admin", form=form)


@student.route("/student_table")
@login_required
def student_table():
    students = Student.query.order_by('study_year')
    return render_template("admin/student_table.html", title="Admin", students=students)



@student.route('/student/login', methods=['GET', 'POST'])
def student_login():
    
    if current_user.is_authenticated:
        return redirect(url_for('student_dashboard'))

    form = StudentLoginForm()
    
    if form.validate_on_submit():
        student = Student.query.filter_by(admission_number=form.admission_number.data).first()

        if student and check_password_hash(student.password, form.password.data):
            login_user(student)
            return redirect(url_for('student_dashboard'))
        else:
            flash(f'Invalid Admission or Password', 'danger')
    return render_template("student/login.html", title="Student", form=form)


#Student dashboard

@student.route('/student/dashboard')
@login_required
def student_dashboard():
    return render_template('student/dashboard.html', title="Student")

@student.route('/student_profile')
@login_required
def student_profile():
    return render_template('student/user.html', title="Student")


#student logout 

@student.route('/student/logout')
@login_required
def student_logout():
    logout_user()
    session.clear()
    flash('Logged Out was Successfull','success')
    return redirect(url_for('home'))

