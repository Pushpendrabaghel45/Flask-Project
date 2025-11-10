from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secretkey123'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/meetingdetails")
def meetingdetails():
    return render_template('meetingdetails.html')

@app.route("/meetings")
def meetings():
    return render_template('meetings.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']  
        subject = request.form['subject']
        message = request.form['message']
        # flash(f"Thank you {name}! Your feedback has been received.")
        # return render_template('feedback.html', name=name, email=email, message=message)
        return render_template('feedback.html', name=name, email=email, subject=subject, message=message, res=(f"Thank you {name}! Your feedback has been received."))
    return redirect(url_for('feedback'))

if __name__ == "__main__":
    app.run(debug=True)
