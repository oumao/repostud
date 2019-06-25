from flask import render_template, url_for, session, flash, redirect
from flask_login import login_required, login_user, logout_user
from repoapp import app, db
from repoapp.forms import AdminRegistrationForm, AdminLoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from repoapp.models import Admin

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home")


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
        return render_template('home.html', title='Home')


@app.route("/admin_login", methods=['POST', 'GET'])
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
    return render_template('admin/dashboard.html', title="Admin")

@app.route("/user_profile")
@login_required
def user_profile():
    return render_template("admin/user.html", title="Admin Profile")
