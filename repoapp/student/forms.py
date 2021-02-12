from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from .models import Admin
from flask_wtf.file import FileField, FileAllowed 
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class StudentRegistrationForm(FlaskForm):

	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	admission_number = StringField('Admission Number', validators=[DataRequired()])
	birth_date = DateField('Year of Birth', format="%Y-%m-%d" )
	gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
	program = SelectField('University Program', choices=[('Computer Science', 'BSc. Computer Science'), ('Statistics', 'BSc. Statistics'), ('Chemistry', 'BSc. Chemistry'), ('Mathematics', 'BSc. Mathematics'), ('Physics', 'BSc. Physics'), ('Fashion and Design', 'BSc. Fashion and Design'), ('Zoology', 'BSc. Zoology'), ('Botany', 'BSc. Botany'), ('Microbiology', 'BSc. Microbiology'), ('Biochemistry', 'BSc. Biochemistry')])
	study_year = SelectField('Year of Study', choices=[('Y1', 'First Year'), ('Y2', 'Second Year'), ('Y3', 'Third Year'), ('Y4', 'Fourth Year')])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])

	submit = SubmitField('Register')

class StudentLoginForm(FlaskForm):
	
	admission_number = StringField('Admission Number', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	
	submit = SubmitField('Login')
