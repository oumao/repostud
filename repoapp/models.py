from datetime import datetime
from repoapp import db

class Admin(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    profile_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Admin({self.fullname}, {self.email}, {self.profile_pic})"


class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    admission_number = db.Column(db.String(80), nullable=False, unique=True)
    birth_date = db.Column(db.DateTime, nullable=False)
    program = db.Column(db.Text, nullable=False)
    study_year = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Student({self.fullname}, {self.admission_number},
         {self.birth_date}, {self.program}, {self.study_year})"


class Lecturer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    staff_number = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Lecturer({self.fullname}, {self.email}, {self.staff_number})"

class Course(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.Text, nullable=False)
    course_code = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"Course({self.course_name}, {self.course_code})"


class Assignment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    assignment_file = db.Column(db.String(40), nullable=False, default='default.jpg')
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Assignment({self.assignment_file})"
    
class SubmittedAssignment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
     