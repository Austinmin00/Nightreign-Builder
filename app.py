from flask import Flask, redirect, render_template, request, session 
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False # Session expires when browser closes
app.config['SESSION_TYPE'] = 'filesystem' # Store sessions in the filesystem
Session(app) # Initialize the session extension

@app.route('/')
def index():
    if not session.get("name"):
        session["name"] = "Guest"
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session["name"] = None
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect('/')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)