from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from ..models import Admin
from flask_wtf.file import FileField, FileAllowed 
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class AdminRegistrationForm(FlaskForm):

	fullname = StringField('Full Name', validators=[DataRequired(), Length(min=6, max=50)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')


class AdminLoginForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')

	submit = SubmitField('Sign In')

class AdminProfileForm(FlaskForm):
	
	fullname = StringField('Full Name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	profile_pic = FileField('Update Profile Picture', validators=[FileAllowed('png', 'jpg')])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm your Password', validators=[DataRequired(), EqualTo('password')])

	submit = SubmitField('Update')
