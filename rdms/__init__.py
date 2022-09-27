from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta


# Initialize flask app
app = Flask(__name__) 

# Set app secret key
# Keep this private!
app.secret_key = 'f2e0c2ac806d947324d5c875ec1cc96dd0a89c88f2a317e6fc23a674697755af'

# Change this URI if you are working with this project on your machine
# Configure database connection 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3325/mysqlproject' 

# Suppress warnings 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure app to remember user login for 180 seconds on browser terminate
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=180)
app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True

# Attach SQLAlchemy to app 
db = SQLAlchemy(app)


from rdms import routes 
