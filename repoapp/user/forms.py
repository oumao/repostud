from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from ..models import User
from flask_wtf.file import FileField, FileAllowed 
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class UserRegistrationForm(FlaskForm):

	first_name = StringField('First Name', validators=[DataRequired(), Length(min=3, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=20)])
	username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')


class UserLoginForm(FlaskForm):

	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')

	submit = SubmitField('Sign In')

class UserProfileForm(FlaskForm):
	
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
	profile_pic = FileField('Update Profile Picture', validators=[FileAllowed('png', 'jpg')])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm your Password', validators=[DataRequired(), EqualTo('password')])

	submit = SubmitField('Update')
