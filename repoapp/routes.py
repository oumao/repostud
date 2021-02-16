import os, secrets
from flask import render_template, url_for, session, flash, redirect, request
from flask_login import login_required, login_user, logout_user, current_user
from repoapp import app, db
from repoapp.forms import (AdminRegistrationForm, AdminLoginForm, AdminProfileForm,
                        StudentRegistrationForm, StudentLoginForm,
                        LecturerRegistrationForm, LecturerLoginForm, CourseRegistrationForm,
                        AssignmentSubmissionForm)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from repoapp.models import Admin, Student, Lecturer, Course, SubmittedAssignment











""" Lecturer Routes """



""" Course Routes """

@app.route("/add_course", methods=['POST', 'GET'])
@login_required
def add_course():

    form = CourseRegistrationForm()

    lect = Lecturer.query.filter_by(staff_number=form.staff_number.data).first()

    if form.validate_on_submit():
        course = Course(course_name=form.course_name.data, course_code=form.course_code.data, lecturer=lect)
        db.session.add(course)
        db.session.commit()
        flash('Successfully assigned the unit', 'success')
        return redirect(url_for('add_course'))

    return render_template("admin/course.html", title="Admin", form=form)


""" Logins for Student and Lecturers """










#Lecturer Login


