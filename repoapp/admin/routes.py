from flask import render_template, url_for, session, flash, redirect, request
from flask_login import login_required, login_user, logout_user, current_user
from repoapp import db
from werkzeug.security import generate_password_hash, check_password_hash
from repoapp.models import User 


from . import admin
from repoapp.admin.forms import AdminLoginForm


@admin.route("/admin/registration", methods=['POST', 'GET'])
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


@admin.route("/admin/login", methods=['POST', 'GET'])
def admin_login():

    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = User.query.filter_by(username=form.username.data).first()

        if admin and check_password_hash(admin.password, form.password.data):
            login_user(admin)
            return redirect(url_for('admin_dashboard'))
        else:
            flash(f'Invalid Email or Password', 'danger')
        
    return render_template('admin/login.html', title="Admin Login", form=form)



@admin.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have successfully Logged Out','success')
    return redirect(url_for('home'))


@admin.route("/admin_dashboard")
@login_required
def admin_dashboard():
    head = Admin.query.all()
    return render_template('admin/dashboard.html', title="Admin", head=head)

@admin.route("/user_profile", methods=['GET', 'POST'])
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