from flask import Flask, render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secretkey123'

users = {}

# ---------------- AUTH ROUTES ---------------- #

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if email in users:
            flash('Email already registered. Please log in.', 'warning')
            return redirect(url_for('login'))

        users[email] = {
            'name': name,
            'email': email,
            'password': generate_password_hash(password)
        }
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users.get(email)
        if user and check_password_hash(user['password'], password):
            session['user'] = user['name']
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password!', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


# ---------------- PAGE ROUTES ---------------- #

@app.route("/")
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', user=session['user'])


@app.route("/meetingdetails")
def meetingdetails():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('meetingdetails.html')


@app.route("/meetings")
def meetings():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('meetings.html')


@app.route('/feedback')
def feedback():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('feedback.html')





@app.route('/submit', methods=['POST'])
def submit():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']  
        subject = request.form['subject']
        message = request.form['message']

        res = f"Thank you {name}! Your feedback has been received."
        return render_template('feedback.html', name=name, email=email, subject=subject, message=message, res=res)
    
    return redirect(url_for('feedback'))


if __name__ == "__main__":
    app.run(debug=True)
