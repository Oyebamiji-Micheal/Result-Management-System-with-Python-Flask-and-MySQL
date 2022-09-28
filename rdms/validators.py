from email_validator import validate_email, EmailNotValidError


def validate_admin_email(admin_email):
    """
    Validate email address

        Conditions:
            Email must be properly formatted (not necessarily exist)
            Email must not end with 'stu.edu.ng'
        Return:
            A tuple consisting two elements. 
            First element is a Boolean value. False means email fails
            condition check while True means otherwise. 
            Second element is an error message stating why the 
            condition fails. 
    """
    try:
        if (validate_email(admin_email, check_deliverability=False) and 
            admin_email.endswith('stu.edu.ng')):
            error_message = 'Admin email must not end with \'stu.edu.ng\''
            return (False, error_message)
    except EmailNotValidError as e:
        return (False, e)
    return (True,)

def validate_student_email(student_email):
    """
    Validate email address

        Conditions:
            Email must be properly formatted (not necessarily exist)
            Email must end with 'stu.edu.ng'
        Return:
            A tuple consisting two elements. 
            First element is a Boolean value. False means email fails 
            condition check while True means otherwise. 
            Second element is an error message stating why the 
            condition fails.  
    """
    try:
        if (validate_email(student_email, check_deliverability=False) and 
            not student_email.endswith('stu.edu.ng')):
            error_message = 'Student email must end with \'stu.edu.ng\''
            return (False, error_message) 
    except EmailNotValidError as e:
        return (False, e)
    return (True,)

def validate_course_code(course_code):
    """
    Validate course code.

    Conditions:
            Course codes should be six characters long.
            The first three characters should be upercase letters. 
            The last three characters should be numbers
        Return:
            A tuple consisting two elements. 
            First element is a Boolean value. False means 
            email fails condition check while True means otherwise. 
            Second element is an error message stating why the 
            condition fails.  
    """
    course_code = course_code.strip()
    first_integer = -1
    for char in course_code:
        if char.isdigit():
            first_integer = int(char)
            break

    if (len(course_code) != 6 or
        not (course_code[:3].isalpha() and course_code[:3].isupper()) or
        not course_code[3:].isdigit()):
        error_message = 'Please follow the convention for adding course codes'
        return (False, error_message, first_integer) 

    return (True,)
    
