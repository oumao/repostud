from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from .models import Lecturer
from flask_wtf.file import FileField, FileAllowed 
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class LecturerRegistrationForm(FlaskForm):

	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	staff_number = StringField('Staff Number', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

	submit = SubmitField('Register')


	def validate_username(self, username):
		lect = Lecturer.query.filter_by(username=username.data).first()
		if lect:

			raise ValidationError("Username already Exists try another one")


	def validate_email(self, email):
		lect = Lecturer.query.filter_by(email=email.data).first()
		if lect:
			raise ValidationError("Email already in user try another one")

class LecturerLoginForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])

	submit = SubmitField('Login')


