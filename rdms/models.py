from flask import abort, flash, request, redirect, url_for,render_template
from flask_login import LoginManager, UserMixin, current_user
from werkzeug.security import generate_password_hash

from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from datetime import datetime

from rdms.validators import validate_student_email, validate_admin_email 
from rdms.validators import validate_course_code

from rdms import app, db


# Initialize flask admin app with bootstrap4 template 
admin = Admin(app, name='Admin Page', template_mode='bootstrap4')

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# user_loader callback function
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


# Handle unauthorized requests to admin page from users
@app.errorhandler(403)
def not_found_error(error):
    """
    Handle unauthorized requests to admin page from users.
    Render 403.html template
    """
    return render_template('403.html')


# Handle page not found error (404)
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle page not found error (404)
    Render 404.html template
    """
    return render_template('404.html')  


class Users(UserMixin, db.Model):
    """
    Create a 'users' table which contains both students and admins 
    email and password.

    Attributes:
        id (int): Primary key 
        email (str): Admin or Student email 
        password (str): Hashed user password. Set default to 1234 when 
                        admin creates new user
        admin (bool): True if user is an admin and False otherwise
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(1000), 
                         default=generate_password_hash('1234'))
    admin = db.Column(db.Boolean, nullable=False)

    def __repr__(self) -> str:
        # Return the user's email as string representation of the user object
        return f'{self.email}'


class Students(db.Model):
    """
    Create 'students' table which contains students emails only. 
    This table has a one to one relationship with 'profiles' table.
    Thus it enforces that profiles are created for student 
    accounts that actually exist.   

    Attributes:
        id (int): Primary key 
        email (str): Email of student or admin
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True) 
    # Create a relationship between students and profiles table 
    profile = db.relationship('Profiles', backref='student_email', 
                              uselist=False)

    def __repr__(self) -> str:
        return f'{self.email}'


class Profiles(db.Model):
    """
    Create profile table which contains basic student information.
    This table has a one to many relationship with 'results' table.
    Thus it enforces that results are created only for students whose 
    profile detail exist.  

    Attributes:
        id (int): Primary key 
        name (str): Student full name
        email (str): Student email 
        department (str): Student department
        faculty (str): Student faculty
        level (int): Current level
        sex (str): Student gender
        date_of_birth (str): Student date of birth
        nationality (str): Student nationality
        last_updated (datetime): The last time an admin updates a student 
        profile
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(
        db.String(100), db.ForeignKey('students.email'), nullable=False, 
        unique=True
    )
    faculty = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    nationality = db.Column(db.String(100), nullable=False, default='Nigerian')
    last_updated = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow
    )
    student_details = db.relationship('Results', backref='student_detail')

    def __repr__(self) -> str:
        return f'{self.email} {self.level} {self.department}'
    

class Results(db.Model):
    """
    Create student results table.  

    Attributes:
        id (int): Primary key 
        email (str): Student email
        code (str): Course code
        description (str): Course description
        result (int): Course score
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(
        db.String(100), db.ForeignKey('profiles.email'), nullable=False
    )
    code = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    result = db.Column(db.Integer, nullable=False) 

    def __repr__(self) -> str:
        return f'{self.email}'


class CourseView(BaseView):
    """Extend BaseView class."""

    # Add new url endpoint '/admin/courses'
    @expose('/')
    def index(self):
        return self.render('courses.html')


class UsersView(ModelView):
    """Overide certain ModelView class attributes."""

    # Admin cannot delete nor edit data from 'users' table
    can_delete = False
    can_edit = False

    # Use 'admin' column as default column sort 
    column_default_sort = ('admin', False)
    
    # Make 'password' field read only.
    form_widget_args = {
        'password': {
            'readonly': True
        }
    }

    # Admins only can access this page and they must logged in 
    def is_accessible(self):
        """
        Validate users before giving them access to the admin page
        Conditions:
            User must be logged in
            User must be an Admin
        """
        if current_user.is_authenticated and current_user.admin == True:
            return current_user.is_authenticated
        else:
            return abort(403) 

    def validate_form(self, form):
        """
        Validate form on submit. 
        Import validate_admin_email and validate_student_email funtions 
        from validators.py. Both functions return a tuple. 
        First element is a Boolean value. False means email fails 
        condition check while True means otherwise. 
        Second element is an error message stating why the condition fails.
        
        Conditions:
            Admin:
                Email must be properly formatted (not necessarily exist)
                Only validate on form submit 
                Email must not end with 'stu.edu.ng'
            Student:
                Email must be properly formatted (not necessarily exist)
                Only validate on form submit 
                Email should end with 'stu.edu.ng'
        """
        try:
            # Admin email validation
            # User must be an admin and validate only on form submit
            if form.admin.data == True and form.email.data != None:
                admin_validations = validate_admin_email(form.email.data)
                if not admin_validations[0]:
                    flash(f'{admin_validations[1]}', 'error')
                    return False
            # User must be a Student and validate only on form submit
            elif form.admin.data == False and form.email.data != None:
                student_validations = validate_student_email(form.email.data)
                if not student_validations[0]:
                    flash(f'{student_validations[1]}', 'error')
                    return False
            return super(UsersView, self).validate_form(form)
        except AttributeError:
            return super(UsersView, self).validate_form(form)

    # When an admin adds a new student to the database
    # Automatically add the student email to 'students' table if
    # the email ends with 'stu.ui.edu.ng'   
    def after_model_change(self, form, model, is_created):
        """
        For every new student added to 'Users' table,
        automatically add their email address to the 'Students' table 
        """
        newly_added_email = model.email
        # Check if email is a student email
        if newly_added_email.endswith('stu.edu.ng'):
            # add email to students table
            new_student = Students(email=newly_added_email)
            print(new_student)
            db.session.add(new_student)
            db.session.commit() 


class ProfileView(ModelView):
    """Overide certain ModelView class attributes."""

    # Admins can not delete results 
    # I do not want people messing up things
    # Someone can just decide to delete all records! 
    can_delete = False

    form_excluded_columns = ('student_details')

    # Make 'email and 'last_updated' field readonly
    form_widget_args = {
        'student_email': {
            'readonly': True
        },
        'last_updated': {
            'readonly': True
        },
    }

    # Restrict 'sex' and 'level' field input data 
    form_choices = {
            'sex': [
                ('Male', 'Male'), 
                ('Female', 'Female')
            ],
            'level': [
            (100, 100), 
            (200, 200),
            (300, 300),
            (400, 400),
            (500, 500),
            (600, 600)
            ]
        }

    def validate_form(self, form):
        """
        Validate form on submit.

        Conditions:
            Email must be unique
            Only validate form on submit
            Ignore Validation on edit form request
        """
        # get student email from submitted form
        form_email = str(list(form.data.values())[-1])
        # validate only on submit 
        if (request.method == "POST" and 
            # Ignore Validation on edit form request
            'edit' not in request.url and
            # email must be unique i.e. a profile info per student 
            Profiles.query.filter_by(email=form_email).first()):
            flash(f'Student profile already exists for {form_email}', 'error')
            return False
        return super(ProfileView, self).validate_form(form)


class ResultView(ModelView):
    """Overide ModelView class attribute."""

    # Admins can not delete results 
    # I do not want people messing up things
    can_delete = False

    # Use email column as default column sort 
    column_default_sort = ('email', False)

    def validate_form(self, form):
        """
        Validate form on submit.

        Conditions:
            Only validate on form submit
            Result cannot be greater than 100 nor less than 0
        """
        try:
            # validate only on form submit
            if form.result.data != None:
                # validate course code
                code_validations = validate_course_code(form.code.data) 
                # extract student details from submitted form
                student_detail = list(form.data.values())[-1]
                # extract level from student details
                level = str(student_detail).split()[1]
                # flash error message if course code format validation fails
                if not code_validations[0]:
                    flash(f'{code_validations[1]}', 'error')
                    return False
                # Flash error message if course code does 
                # not correspond to level
                if form.code.data[3] != level[0]:
                    flash('Course Code does not correspond to Level', 'error')
                    return False
                # Result should be in the range 0 to 100
                if (form.result.data > 100 or 
                    form.result.data < 0):
                    flash('Result cannot be greater than 100 \
                        nor less than 0 😐', 'error')
                    return False
            return super(ResultView, self).validate_form(form)
        except AttributeError:
            return super(ResultView, self).validate_form(form)


class StudentView(ModelView):
    """Overide certain ModelView class attributes."""

    # Admins cannot delete or edit or create data
    # Recall that students emails are automatically 
    # added once their login details are defined in 'users' table
    can_delete = False
    can_edit = False
    can_create = False


# Add modelviews for managing database models 
admin.add_view(UsersView(Users, db.session, 
               menu_icon_type='fa', menu_icon_value='fa-users'))
admin.add_view(StudentView(Students, db.session, 
               menu_icon_type='fa', menu_icon_value='fa-list')) 
admin.add_view(ProfileView(Profiles, db.session, 
               menu_icon_type='fa', menu_icon_value='fa-pencil')) 
admin.add_view(ResultView(Results, db.session, 
               menu_icon_type='fa', menu_icon_value='fa-book'))
admin.add_view(CourseView(name='Courses', endpoint='courses', 
               menu_icon_type='fa', menu_icon_value='fa-database'))