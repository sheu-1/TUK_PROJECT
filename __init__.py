from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

import os

load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equity.db'  # Add this line here
app.app_context().push()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'alexsheunda@gmail.com'
app.config['MAIL_PASSWORD'] = '13735524Aa.'
app.config['MAIL_DEFAULT_SENDER'] = 'alexsheunda@gmail.com'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)

# Flask-Login settings
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Define the user_loader callback
@login_manager.user_loader
def load_user(user_id):
    from final_year.models import User  # Import User inside the function to avoid circular import issues
    return User.query.get(int(user_id))

# Import models at the end to avoid circular imports
from final_year.models import User, Appointment

# Import the routes module
from final_year import routes