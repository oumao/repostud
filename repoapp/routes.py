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




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home")


""" Administrator Routes from Here """

@app.route("/admin/registration", methods=['POST', 'GET'])
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
        flash("Administrator has already been registered into the system. Kindly login to continue!", "danger")
        return render_template('home.html', title='Home')


@app.route("/admin/login", methods=['POST', 'GET'])
def admin_login():

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
    head = Admin.query.all()
    return render_template('admin/dashboard.html', title="Admin", head=head)

@app.route("/user_profile", methods=['GET', 'POST'])
@login_required
def user_profile():

    hod = Admin.query.filter_by(email=Admin.email).first()

    form = AdminProfileForm()

    if form.validate_on_submit():
        hod.fullname = form.fullname.data
        hod.email = form.email.data
        hod.password = generate_password_hash(form.password.data)

        db.session.commit()
        flash('Your account has been successfully updated', 'success')
        return redirect(url_for('admin_dashboard'))
       
    profile_pic = url_for('static', filename='assets/img/faces/' + hod.profile_pic) 
    
    return render_template("admin/user.html", title="Admin", form=form, profile_pic=profile_pic)


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
    students = Student.query.order_by('study_year')
    return render_template("admin/student_table.html", title="Admin", students=students)


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

    lecs = Lecturer.query.all()
    return render_template("admin/lecturer_table.html", title="Admin", lecs=lecs)



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

@app.route('/student/login', methods=['GET', 'POST'])
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

@app.route('/student/dashboard')
@login_required
def student_dashboard():
    return render_template('student/dashboard.html', title="Student")

@app.route('/student_profile')
@login_required
def student_profile():
    return render_template('student/user.html', title="Student")


#student logout 

@app.route('/student/logout')
@login_required
def student_logout():
    logout_user()
    session.clear()
    flash('Logged Out was Successfull','success')
    return redirect(url_for('home'))




def allowed_file(filename):

    if not '.' in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.lower()  in app.config['ALLOWED_FILE_EXTENSIONS']:
        return True
    else: 
        return False
    


@app.route('/submitted_assignment', methods=['GET', 'POST'])
@login_required
def submitted_assignment():
    
        
    form = AssignmentSubmissionForm()

    cour = Course.query.filter_by(course_code=form.course_code.data).first()
    stud = Student.query.filter_by(admission_number=current_user.admission_number).first()

    if request.method == "POST":

        if request.files:

            ass_file = request.files['submitted_file']

            if ass_file.filename == "":
                flash("File should have a Name", "danger")
                return redirect(url_for('submitted_assignment'))

            if not allowed_file(ass_file.filename):
                flash("The file extension is not allowed", "danger")
                return redirect(url_for('submitted_assignment'))

            else:

                filename = secure_filename(ass_file.filename)
                ass_file.save(os.path.join(app.config['SUBMITTED_ASSIGNMENT'], filename))

        if form.validate_on_submit():
            flash("The file is Successfully Uploaded ", "success")
            print(filename)

        sub_ass = SubmittedAssignment(submitted_file=filename, score=0, student=stud, course=cour)
        db.session.add(sub_ass)
        db.session.commit()
        flash('Successfully Uploaded your file', 'success')
        return redirect(url_for('submitted_assignment', ass_file=ass_file))

    
    
    return render_template('student/assignment.html', form=form)


@app.route('/assignment/table', methods=['GET', 'POST'])
def assignment_table():

    ass_results = db.session.query(Course.course_code, Course.course_name, SubmittedAssignment.submitted_file).outerjoin(Course, SubmittedAssignment.course_id == Course.id).all()
    
    return render_template('student/assignment_table.html', title="Student", ass_results=ass_results)



#Lecturer Login

@app.route('/lecturer_login', methods=['GET', 'POST'])
def lecturer_login():
    form = LecturerLoginForm()
    return render_template("lecturer/login.html", title="Lecturer", form=form)

