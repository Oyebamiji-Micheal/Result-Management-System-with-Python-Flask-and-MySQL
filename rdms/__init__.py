from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta


# Initialize flask app
app = Flask(__name__) 

# Set app secret key
# Keep this private!
app.secret_key = '**********'

# Change this URI if you are working with this project on your machine
# Configure database connection 
app.config['SQLALCHEMY_DATABASE_URI'] = '**********'

# Suppress warnings 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure app to remember user login for 180 seconds on browser terminate
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=180)
app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True

# Attach SQLAlchemy to app 
db = SQLAlchemy(app)


from rdms import routes 
