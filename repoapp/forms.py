from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileAllowed 
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

""" Administrator Forms """

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


""" Student Forms """

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


""" Lecturer Forms """

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



""" Course and Assignment Forms """



class CourseRegistrationForm(FlaskForm):

	course_name = StringField('Course', validators=[DataRequired()])
	course_code = StringField('Course Code', validators=[DataRequired()])
	staff_number = StringField('Staff Number', validators=[DataRequired()])

	submit = SubmitField('Register Course')



class AssignmentSubmissionForm(FlaskForm):

	course_code = SelectField('Course Code', choices=[('COM 100', 'COM 100'), ('STA 205','STA 205'), ('CHEM 210', 'CHEM 210'), ('CHEM 323', 'CHEM 323'), ('COM 111', 'COM 111')])
	course_name = SelectField('Course', choices=[('Introduction to Computers', 'Introduction to Computers'), ('Statistics and Probability', 'Statistics and Probability'), ('Analytical Chemistry', 'Analytical Chemistry'), ('Organic Chemistry I', 'Organic Chemistry I'), ('Internet Applications', 'Internet Applications')])
	submitted_file = FileField('Your Assignment File', validators=[FileAllowed('docx', 'pdf')] )

	submit = SubmitField('Upload')
