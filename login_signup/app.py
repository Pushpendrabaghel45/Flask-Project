from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Flask setup
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # needed for flash & session
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create tables (run once)
with app.app_context():
    db.create_all()

# ---------- ROUTES ----------

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# print("called out side")
# SIGNUP
# print("get4")
@app.route('/signup', methods=['POST'])
# @app.route('/', methods=['POST'])
def signup():
    print("get")
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    print(email)
    # Check if user exists
    user = User.query.filter_by(email=email).first()
    print("get")
    print(user)
    if user:
        flash('Email already exists. Please login!', 'warning')
        return redirect(url_for('home'))

    # Create new user
    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    flash('Signup successful! Please login now.', 'success')
    return redirect(url_for('home'))

# LOGIN
print("get4")
@app.route('/signin', methods=['GET', 'POST'])
def login():
    print("get")
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Invalid credentials. Try again.', 'danger')
        return redirect(url_for('home'))

    # signin success
    session['user_id'] = user.id
    session['name'] = user.name
    flash(f'Welcome, {user.name}!', 'success')
    return redirect(url_for('dashboard'))

# DASHBOARD
# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' not in session:
#         return redirect(url_for('home'))
#     return f"<h2>Welcome, {session['user_name']}! You are logged in.</h2><br><a href='/logout'>Logout</a>"

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    return render_template('dashboard.html', name=session['name'])


# LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))
    

if __name__ == '__main__':
    app.run(debug=True)
