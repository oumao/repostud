from flask import render_template, url_for, session, flash, redirect, request
from flask_login import login_required, login_user, logout_user, current_user
from repoapp import app, db
from repoapp.forms import UserRegistrationForm, UserLoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from repoapp.models import User 



@user.route("/user/add_user", methods=['POST', 'GET'])
def add_user():
    
    form = UserRegistrationForm()

    if form.validate_on_submit():
        hash_pass = generate_password_hash(form.password.data)
        new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, 
                        username=form.username.data, gender=form.gender.data, 
                        email=form.email.data, password=hash_pass )

        db.session.add(new_user)
        db.session.commit()
        flash('User successfully registered!', 'success')
        return redirect(url_for('add_user'))
    return render_template("admin/student.html", title="Admin", form=form)
