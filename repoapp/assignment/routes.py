

@assign.route('/assignment/table', methods=['GET', 'POST'])
def assignment_table():

    ass_results = db.session.query(Course.course_code, Course.course_name, 
                            SubmittedAssignment.submitted_file)
                    .outerjoin(Course, SubmittedAssignment.course_id == Course.id)
                    .all()
    
    return render_template('student/assignment_table.html', title="Student", ass_results=ass_results)


def allowed_file(filename):

    if not '.' in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.lower()  in app.config['ALLOWED_FILE_EXTENSIONS']:
        return True
    else: 
        return False
    


@assign.route('/submitted_assignment', methods=['GET', 'POST'])
@login_required
def submitted_assignment():
        
    form = AssignmentSubmissionForm()

    cour = Course.query.filter_by(course_code=form.course_code.data).first()
    stud = Student.query.filter_by(admission_number=current_user.admission_number).first()

    if request.method == "POST":

        if request.files:

            ass_file = request.files['submitted_file']

            if ass_file.filename == "":
                flash("File should have a Name", "danger")
                return redirect(url_for('submitted_assignment'))

            if not allowed_file(ass_file.filename):
                flash("The file extension is not allowed", "danger")
                return redirect(url_for('submitted_assignment'))

            else:

                filename = secure_filename(ass_file.filename)
                ass_file.save(os.path.join(app.config['SUBMITTED_ASSIGNMENT'], filename))

        if form.validate_on_submit():
            flash("The file is Successfully Uploaded ", "success")
            print(filename)

        sub_ass = SubmittedAssignment(submitted_file=filename, score=0, student=stud, course=cour)
        db.session.add(sub_ass)
        db.session.commit()
        flash('Successfully Uploaded your file', 'success')
        return redirect(url_for('submitted_assignment', ass_file=ass_file))

    
    
    return render_template('student/assignment.html', form=form)
