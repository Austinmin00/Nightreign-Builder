import os

from dotenv import load_dotenv

from flask import Flask, redirect, render_template, request, session 
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

class User(db.Model): # Created User model for database
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)    

with app.app_context():
    db.create_all()  # Create database tables

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SESSION_PERMANENT'] = False # Session expires when browser closes
app.config['SESSION_TYPE'] = 'filesystem' # Store sessions in the filesystem
Session(app) # Initialize the session extension

csrf = CSRFProtect(app) # Initialize CSRF protection

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
) # Initialize rate limiting

@app.route('/')
def index():
    if not session.get("name"):
        session["name"] = "Guest"
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("10 per hour")
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if not username or not password:
            return "Enter a username and password", 400
        elif user and check_password_hash(user.password, password):
            session["name"] = username
            return redirect('/')
        else:
            return "Invalid username or password", 400
    return render_template('login.html')

@app.route('/logout')
def logout():
    session["name"] = None
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
@limiter.limit("5 per hour")
def register():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            return "Passwords do not match", 400
        elif User.query.filter_by(username=user).first():
            return "Username already exists", 400
        elif not user or not password:
            return "Enter a username and password", 400
        else:
            hashed_password = generate_password_hash(password, method='scrypt', salt_length=16)
            new_user = User(username=user, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)