from flask import render_template, url_for, session, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from repoapp import app, db
from repoapp.forms import AdminRegistrationForm, AdminLoginForm, StudentRegistrationForm, LecturerRegistrationForm, CourseRegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from repoapp.models import Admin, Student, Lecturer, Course


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home")


""" Administrator Routes from Here """

@app.route("/admin_registration", methods=['POST', 'GET'])
def admin_registration():
    
    user_exist = Admin.query.all()
    if not user_exist:
        form = AdminRegistrationForm()
        if form.validate_on_submit():
            hash_pass = generate_password_hash(form.password.data)
            admin = Admin(fullname=form.fullname.data, email=form.email.data, password=hash_pass) 
            db.session.add(admin)
            db.session.commit()
            
            flash(f"Your account has been created!", "success")
            return redirect(url_for('admin_login'))
        return render_template('admin/registration.html', title="Admin Registration", form=form)
    else:
        flash("Administrator has already been registered into the system. \
            Kindly login to continue!", "danger")
        return render_template('home.html', title='Home')


@app.route("/admin_login", methods=['POST', 'GET'])
def admin_login():

    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))

    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()

        if admin and check_password_hash(admin.password, form.password.data):
            login_user(admin)
            return redirect(url_for('admin_dashboard'))
        else:
            flash(f'Invalid Email or Password', 'danger')
        
    return render_template('admin/login.html', title="Admin Login", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have successfully Logged Out','success')
    return redirect(url_for('home'))


@app.route("/admin_dashboard")
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html', title="Admin")


@app.route("/user_profile")
@login_required
def user_profile():
    return render_template("admin/user.html", title="Admin")


""" Student Routes """

@app.route("/add_student", methods=['POST', 'GET'])
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


@app.route("/student_table")
@login_required
def student_table():
    return render_template("admin/student_table.html", title="Admin")


""" Lecturer Routes """

@app.route("/add_lecturer", methods=['POST', 'GET'])
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


@app.route("/lecturer_table")
@login_required
def lecturer_table():
    return render_template("admin/lecturer_table.html", title="Admin")



""" Course Routes """

@app.route("/add_course", methods=['POST', 'GET'])
@login_required
def add_course():

    form = CourseRegistrationForm()

    lect = Lecturer.query.filter_by(first_name="Nixon").first()

    if form.validate_on_submit():
        course = Course(course_name=form.course_name.data, course_code=form.course_code.data, lecturer=lect)
        db.session.add(course)
        db.session.commit()
        flash('Successfully assigned the unit', 'success')
        return redirect(url_for('add_course'))

    return render_template("admin/course.html", title="Admin", form=form)


