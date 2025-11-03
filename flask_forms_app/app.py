from flask import Flask , render_template, request, flash

app = Flask(__name__)
app.secret_key = 'secretkey123'



@app.route('/')
def index():
    return render_template('feedback.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    flash(f"Thank you {name}! Your feedback has been received.")
    return render_template('feedback.html', name=name, message=message)

if __name__ == '__main__':
    app.run(debug=True)
