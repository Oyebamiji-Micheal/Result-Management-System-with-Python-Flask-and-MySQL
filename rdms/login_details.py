def details():
    """
    Define students and admin login details.
    Conditions:
        Admin emails should not end with 'stu.edu.ng'.
        Students emails must end with 'stu.edu.ng'.
        'False' indicates that user is a student.
        'True' indicates that user is an admin.
        Do not violate the above conditions else the app will not run
        correctly.
    """
    student_details = {
        'mjane@stu.edu.ng': ('1234', False), 'oprecious@stu.edu.ng': ('4321', False),
        'apaul@stu.edu.ng': ('0000', False), 'jtobi@stu.edu.ng': ('0000', False), 
        'ajeremiah@stu.edu.ng': ('1234', False), 'cpatterson@stu.edu.ng': ('1234', False),
        'gzion@stu.edu.ng': ('0000', False), 'msmith@stu.edu.ng': ('5678', False), 
        'penoch@stu.edu.ng': ('1234', False), 'rsimon@stu.edu.ng': ('0000', False)
    }
               
    admin_details = {
        'stephen@gmail.com': ('streetcoder', True), 'ajiboyede@gmail.com': ('password', True),
        'omotosho@gmail.com': ('habyaad', True), 'goodness@gmail.com': ('devops', True), 
        'jesutobi@gmail.com': ('bts', True), 'johnsmith@gmail.com': ('thematrix', True)
    }

    return student_details, admin_details 