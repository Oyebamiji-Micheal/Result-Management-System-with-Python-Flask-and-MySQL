# Result Management System with Python Flask and MySQL
<br>

<a href="https://rmsnigeria.pythonanywhere.com/" target="_blank">https://rmsnigeria.pythonanywhere.com/
</a>
<br>

<img src="https://github.com/Oyebamiji-Micheal/Result-Management-System-with-Python-Flask-and-MySQL/blob/master/images/admin_resized.png">

<br>

## Table of Contents
* [Introduction](#intro)
* [Functionalities and Limitations](#limitations)
* [App Structure and Implementation](#structure)
* [Student and Admin Guide](#guide)
* [Running Locally](#local)
* [Contributing](#contribute)
* [Terms and Conditions](#terms)
* [Resources](#resources)
  
<a id='intro'></a>
## Introduction
<p align="justify">
This website is a result of 100 days of SQL challenge I started a few weeks ago and is aimed at practicing and demonstrating the understanding of basic SQl operations. During the course of building this project, I learned how to connect to local and external databases, define tables and relationships, filter database and so on. Also, a significant amount of energy was expended on learning the required concepts, frameworks, languages, and modules. Some of these include HTML, CSS, Flask, SQLAlchemy, Bootstrap, Object Oriented Programming, Virtual Environments, and so on. Although this app has a lot of limitations, I'd say it was worth building. 🙂 
</p>
<br>

<a id='limitations'></a>
## Functionalities and Limitations
<p align="justify">
This website is meant to simulate a real-world result management system whereby students can check their results using their student email and password which has been predefined by the university result management system. Admins are responsible for editing and adding new students' results along with their profile information. This site does not implement functionalities such as
- Changing admin and student passwords. Passwords are predefined.
- Validating if admin emails exist.
- Checking if students offer the specified course code and title.
<br><br>
</p>


<a id='structure'></a>
## App Structure and Implementation
<p align="justify">
This project is implemented in Python and organized as a simple package using the <a href="https://flask.palletsprojects.com/en/2.2.x/patterns/packages/" target="_blank">recommended format</a> for 'large flask applications'.
</p>

📁rdms/ <br>
&emsp; \__init__.py <br>
&emsp; models.py <br>
&emsp; routes.py <br>
&emsp; database scripts <br>
&emsp; validators.py <br>
&emsp; 📁static/ <br>
&emsp;&emsp; 📁admin/ <br>
&emsp;📁templates/ <br>
&emsp; &emsp; 📁admin/ <br>
run.py

<p align="justify"> 
MySQL database and Xampp server was used while working on this project locally. I only used Xampp to create the database and view tables. The Python file `login_details.py` contains both student and admin login details (email and password) while  `define_details.py` contains a script to add the details to the database using Flask SQLAlchemy. 
</p>
<br>

<a id='guide'></a>
## Student and Admin Guide
You can find the website's usage guide [here](https://github.com/Oyebamiji-Micheal/Result-Management-System-with-Python-Flask-and-MySQL/blob/master/guide.md).
<br><br>

<a id='local'></a>
## Running Locally 
<p align="justify">
Python 3.10.6 was used at the time of building this project. For Windows users, make sure Python is added to your PATH.  <br>
Virtual environment. It is advisable to run this project inside of a virtual environment to avoid messing with your machine's primary dependencies. To get started, navigate to this project's directory, <code>Result-Management-System-with-Python-Flask-and-MySQL</code>, on your local machine. Then...
</p>

### 1. Create an environment <br>
**Windows** (cmd) <br>
```
cd Result-Management-System-with-Python-Flask-and-MySQL
pip install virtualenv
python -m virtualenv venv
```
or
```
python3 -m venv venv
```

**macOS/Linux** <br>
```
cd Result-Management-System-with-Python-Flask-and-MySQL
pip install virtualenv
python -m virtualenv venv
```

### 2. Activate environment <br>
**Windows** (cmd)

```
venv\scripts\activate
```

**macOS/Linux**

```
. venv/bin/activate
```
or
```
source venv/bin/activate
```

### 3. Install the Requirements
Windows/macOS/Linux <br>
```pip install -r requirements.txt```

### 4. Create a Database Connection
<p align="justify">
I used Xampp server to create a base. Then used Flask-SQLAlchemy along with a MySQL database to set up connections and define tables. You can use your own local or external database. But first, you need to create the database somewhere and configure its connection to the app in <code>__init__.py</code> file. For a complete list of connection URIs head over to the SQLAlchemy documentation under <a href="https://docs.sqlalchemy.org/en/14/core/engines.html" target="_blank">Supported Database</a>. This here shows some common connection strings.

SQLAlchemy indicates the source of an Engine as a URI combined with optional keyword arguments to specify options for the Engine. The form of the URI is:

```dialect+driver://username:password@host:port/database```

Many of the parts in the string are optional. If no driver is specified the default one is selected (make sure to not include the + in that case).

PostgreSQL <br>
```postgresql://scott:tiger@localhost/project``` 

MySQL / MariaDB <br>
```mysql://scott:tiger@localhost/project```

SQLite (note that platform path conventions apply): <br>
Unix/Mac (note the four leading slashes) <br>
```sqlite:////absolute/path/to/foo.db```

Windows (note 3 leading forward slashes and backslash escapes) <br>
```sqlite:///C:\\absolute\\path\\to\\foo.db```

Windows (alternative using raw string) <br>
```r'sqlite:///C:\absolute\path\to\foo.db'```
</p>

### 5. Create Tables and Define Login Details
<p align="justify">
Once you have created and connected to your database, the next step is to create all tables used in the application by running the code below 

```
>>> from rdms import db
>>> db.create_all()
```

Login details. The login details for admins and students is not added automatically. To use your own custom login details, edit the emails and passwords in ```define_details.py```. Lastly, to add the details to the database, edit the database connection in ```login_details.py``` then run the file.
</p>

### 6. Run app
Windows/macOS/Linux <br>
Make sure you are in this project's root directory then run the command below <br>
```python run.py```

<a id='contribute'></a>
## Contributing
<p align="justify">
    Submit a pull request if you suspect a bug or would like to add to the functionalities of this project.
</p>

<a id='terms'></a>
## Terms and Conditions
* As an admin, I will not mess up or populate the database with messy data. 😶
* I will use descriptive course codes and title. 

<a id='resources'></a>
## Resources
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
<br>

<img src="https://pbs.twimg.com/media/FdvOGhYWYAApxKW?format=jpg&name=900x900">
