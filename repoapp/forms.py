from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from .models import Lecturer
from flask_wtf.file import FileField, FileAllowed 
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError




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
