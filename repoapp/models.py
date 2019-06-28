from datetime import datetime
from repoapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

student_courses = db.Table('student_courses',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)


class Admin(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    profile_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(120), nullable=False)
    

    def __repr__(self):
        return f"Admin({self.fullname}, {self.email}, {self.profile_pic})"


class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    admission_number = db.Column(db.String(80), nullable=False, unique=True)
    birth_date = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    program = db.Column(db.Text, nullable=False)
    study_year = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    submitted_assignments = db.relationship('SubmittedAssignment', backref='student', lazy='dynamic')
    courses = db.relationship('Course',
                            secondary=student_courses,
                            backref=db.backref('student', lazy='dynamic'),
                            lazy='dynamic')

    def __repr__(self):
        return f"Student({self.fullname}, {self.admission_number}, {self.birth_date}, {self.program}, {self.study_year})"


class Lecturer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    staff_number = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    courses = db.relationship('Course', backref='lecturer', lazy='dynamic')

    def __repr__(self):
        return f"Lecturer({self.fullname}, {self.email}, {self.staff_number})"

class Course(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.Text, nullable=False)
    course_code = db.Column(db.String(20), nullable=False, unique=True)
    is_assigned = db.Column(db.Boolean, nullable=False, default=False)
    lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'), nullable=False)
    assignments = db.relationship('Assignment', backref='course', lazy=True)
    assignment_submitted = db.relationship('SubmittedAssignment', backref='course', lazy='dynamic')

    def __repr__(self):
        return f"Course({self.course_name}, {self.course_code})"


class Assignment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    assignment_file = db.Column(db.String(40), nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __repr__(self):
        return f"Assignment({self.assignment_file})"
    
class SubmittedAssignment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    submitted_file = db.Column(db.String(40), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    

    def __repr__(self):
        return f"SubmittedAssignment({self.submitted_file}, {self.score})"