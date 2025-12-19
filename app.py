import os # For accessing environment variables used with database and secret key
from db import db # Database instance from db.py
from dotenv import load_dotenv # Load environment variables from .env file
from flask import Flask, flash, jsonify, redirect, render_template, request, session # Flask web framework and session management
from flask_limiter import Limiter # Rate limiting extension for Flask and routes that handle user login and registration
from flask_limiter.util import get_remote_address # Rate limiting to protect login and registration routes
from flask_session import Session # Server-side session management
from flask_sqlalchemy import SQLAlchemy # Database integration
from flask_wtf.csrf import CSRFProtect # CSRF protection for forms in login and registration routes
from models import Chalice, ChaliceSlot, GuaranteedRelic, RelicEffect, User, Character, WorkshopSession # User model for database interactions
from pydantic import BaseModel, ValidationError, field_validator # for data validation and settings management
from werkzeug.security import generate_password_hash, check_password_hash # for routes that handle user login and registration
load_dotenv() # Load environment variables from .env file

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') # Database connection string from environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Disable modification tracking for performance
db.init_app(app) # Initialize the database extension

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

@app.template_filter('format_name')
def format_name(name):
    """Format chalice names by replacing underscores with spaces, capitalizing words, and adding apostrophes"""
    name = name.replace('_', ' ').title()
    # Add apostrophes for possessives
    name = name.replace('Giants ', "Giant's ")
    return name

@app.route('/')
def index():
    if not session.get("name"):
        session["name"] = "Guest" # Default to 'Guest' if not logged in
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("10 per hour", methods=['POST']) # Limit only POST requests to prevent brute force
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password: # Validate input
            flash("Invalid credentials", "error")
            return render_template('login.html')
        
        user = User.query.filter_by(username=username).first() # Retrieve user from database
        
        # Use constant-time comparison to prevent timing attacks
        if user and check_password_hash(user.password, password): # Check credentials
            # Regenerate session to prevent session fixation
            session.clear()
            session["name"] = username # Log the user in
            session["user_id"] = user.id # Store user ID for authorization
            session.permanent = False # Session expires when browser closes
            return redirect('/')
        else:
            # Generic error message to prevent username enumeration
            flash("Invalid credentials", "error")
            return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear() # Properly clear all session data
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
@limiter.limit("5 per hour", methods=['POST']) # Limit only POST requests for registration
def register():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not user or not password: # Validate input first
            flash("Enter a username and password", "error")
            return render_template('register.html')
        
        if password != confirm_password: # Check password confirmation
            flash("Passwords do not match", "error")
            return render_template('register.html')
        
        try:
            UserModel(username=user, password=password) # Validate user input using Pydantic model
        except ValidationError as e:
            error_msg = e.errors()[0]['msg']  # Extract just the custom error message
            flash(error_msg, "error")
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

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/login')
    user = User.query.get(session['user_id'])
    # return render_template('profile.html', user=user)
    return render_template('index.html', user=user)

@app.route('/workshop')
def workshop():
    selected_character = request.args.get('character')

    if not selected_character:
        return redirect('/')

    character = Character.query.filter_by(key=selected_character.lower()).first()

    if not character:
        return redirect('/')

    # Get global chalices (character_id is NULL)
    global_chalices = Chalice.query.filter_by(character_id=None).all()
    
    # Get character-specific chalices
    character_chalices = Chalice.query.filter_by(character_id=character.id).all()
           
    guaranteed_relics = GuaranteedRelic.query.all()

    relic_effects = RelicEffect.query.all()

    return render_template('workshop.html', character=character, global_chalices=global_chalices, character_chalices=character_chalices, guaranteed_relics=guaranteed_relics, relic_effects=relic_effects)

@app.route('/api/chalice-slots/<chalice_name>')
def get_chalice_slots(chalice_name):
    """API endpoint to get slot colors for a specific chalice"""
    # Convert the formatted name back to database format (e.g., "Giant's Cradle" -> "giants_cradle")
    db_name = chalice_name.lower().replace(' ', '_').replace("'", '')
    
    # Find the chalice by name
    chalice = Chalice.query.filter_by(name=db_name).first()
    
    if not chalice:
        return jsonify({'error': 'Chalice not found'}), 404
    
    # Get the slots for this chalice, ordered by slot_index
    slots = ChaliceSlot.query.filter_by(chalice_id=chalice.id).order_by(ChaliceSlot.slot_index).all()
    
    # Return the colors as a list
    slot_colors = [slot.color for slot in slots]
    
    return jsonify({'id': chalice.id, 'colors': slot_colors})

@app.route('/api/relic-effects')
def get_relic_effects():
    """API endpoint to get all relic effects"""
    # Query all relic effects from the database
    effects = RelicEffect.query.all()

    # Convert database objects to JSON-friendly dictionaries
    effects_data = [
        {
            'id': effect.id,
            'type': effect.type,
            'description': effect.description,
            'effect': effect.effect,
            'stackable': effect.stackable,
            'notes': effect.notes,
            'is_deep': effect.is_deep
        }
        for effect in effects
    ]

    # Return as JSON
    return jsonify(effects_data)

@app.route('/api/guaranteed-relics')
def get_guaranteed_relics():
    """API endpoint to get all guaranteed (sovereign/remembrance) relics"""
    relics = GuaranteedRelic.query.all()
    
    # Convert database objects to JSON-friendly dictionaries
    relics_data = [
        {
            'id': relic.id,
            'name': relic.name,
            'color': relic.color,
            'effect_1': relic.effect_1,
            'effect_2': relic.effect_2,
            'effect_3': relic.effect_3,
            'amount_of_effects': relic.amount_of_effects,
            'is_rememberance': relic.is_rememberance
        }
        for relic in relics
    ]
    
    return jsonify(relics_data)

@app.route('/api/save-workshop', methods=['POST'])
def save_workshop():
    """API endpoint to save workshop configuration"""
    
    data = request.get_json()
    
    # Get user_id from session (None for guests)
    username = session.get('name')
    user_id = None
    if username and username != 'Guest':
        user = User.query.filter_by(username=username).first()
        if user:
            user_id = user.id
    
    # Extract data from request
    character_id = data.get('character_id')
    chalice_id = data.get('chalice_id')
    slot_relics = data.get('slotConfig')  # This should be the slotConfig object with slots 0-5
    
    if not character_id or slot_relics is None:
        return jsonify({'status': 'error', 'message': 'Missing required data'}), 400
    
    # Find existing session or create new one
    workshop_session = WorkshopSession.query.filter_by(
        user_id=user_id,
        character_id=character_id
    ).first()
    
    if workshop_session:
        # Update existing session
        workshop_session.chalice_id = chalice_id
        workshop_session.slot_relics = slot_relics
    else:
        # Create new session
        workshop_session = WorkshopSession(
            user_id=user_id,
            character_id=character_id,
            chalice_id=chalice_id,
            slot_relics=slot_relics
        )
        db.session.add(workshop_session)
    
    db.session.commit()
    
    return jsonify({'status': 'success', 'session_id': workshop_session.id}), 200

@app.route('/relics')
def relics():
    return render_template('relic.html')

@app.route('/news')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)