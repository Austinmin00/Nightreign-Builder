import os # For accessing environment variables used with database and secret key

from dotenv import load_dotenv # Load environment variables from .env file

from flask import Flask, flash, redirect, render_template, request, session # Flask web framework and session management
from flask_limiter import Limiter # Rate limiting extension for Flask and routes that handle user login and registration
from flask_limiter.util import get_remote_address # Rate limiting to protect login and registration routes
from flask_session import Session # Server-side session management
from flask_sqlalchemy import SQLAlchemy # Database integration
from flask_wtf.csrf import CSRFProtect # CSRF protection for forms in login and registration routes
from pydantic import BaseModel, ValidationError, field_validator # for data validation and settings management
from werkzeug.security import generate_password_hash, check_password_hash # for routes that handle user login and registration
load_dotenv() # Load environment variables from .env file

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') # Database connection string from environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Disable modification tracking for performance
db = SQLAlchemy(app) # Initialize the database extension

class UserModel(BaseModel): # Pydantic model for user data validation, must be before User class
    username: str
    password: str
    
    @field_validator('password')
    def password_length(cls, value):
        errors = []
        if len(value) < 12:
            errors.append("at least 12 characters")
        if sum(char.isdigit() for char in value) < 2:
            errors.append("at least two digits")
        if not any(char.isupper() for char in value):
            errors.append("at least one uppercase letter")
        if not any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in value):
            errors.append("at least one special character")
        
        if errors:
            raise ValueError("Password must contain: " + ", ".join(errors))
        
        return value
    
class User(db.Model): # Created User model for database
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  


with app.app_context():
    db.create_all()  # Create database tables

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # Secret key for session management and CSRF protection
app.config['SESSION_PERMANENT'] = False # Session expires when browser closes
app.config['SESSION_TYPE'] = 'filesystem' # Store sessions in the filesystem
Session(app) # Initialize the session extension

csrf = CSRFProtect(app) # Initialize CSRF protection and must be after app initialization and session key setup

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
) # Initialize rate limiting and must be after app initialization

@app.route('/')
def index():
    if not session.get("name"):
        session["name"] = "Guest" # Default to 'Guest' if not logged in
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
# @limiter.limit("10 per hour") # limit login attempts to 10 every hour
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first() # Retrieve user from database

        if not username or not password: # Validate input
            flash("Enter a username and password", "error")
            return render_template('login.html')
        elif user and check_password_hash(user.password, password): # Check credentials
            session["name"] = username # Log the user in
            return redirect('/')
        else:
            flash("Invalid username or password", "error")
            return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session["name"] = None # Log the user out
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
# @limiter.limit("5 per hour") # Limit registration attempts to 5 every hour 
def register():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password: # Check password confirmation
            flash("Passwords do not match", "error")
            return render_template('register.html')
        
        try:
            UserModel(username=user, password=password) # Validate user input using Pydantic model
        except ValidationError as e:
            error_msg = e.errors()[0]['msg']  # Extract just the custom error message
            flash(error_msg, "error")
            return render_template('register.html')

        if not user or not password: # Validate input 
            flash("Enter a username and password", "error")
            return render_template('register.html')

        if User.query.filter(User.username.ilike(user)).first(): # Check if username is a duplicate
            flash("Username already exists", "error")
            return render_template('register.html')

        # If all pass, hash and save
        hashed_password = generate_password_hash(password, method='scrypt', salt_length=16) # Encrypt password for user security
        new_user = User(username=user, password=hashed_password) # Create new user instance
        db.session.add(new_user) # Add new user to the database named 'users'
        db.session.commit() # Commit changes to the database
        return redirect('/login')
    return render_template('register.html')

@app.route('/workshop')
def workshop():
    return render_template('workshop.html')

@app.route('/relics')
def relics():
    return render_template('relic.html')

@app.route('/news')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)