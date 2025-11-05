from flask import Flask, render_template
from forms import UserForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    name = None
    email = None
    password = None
    message = None

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        message = form.message.data
        form.name.data = ''
        form.email.data = ''
        form.password.data = ''
        form.message.data = ''

    return render_template('index.html', form=form, name=name, email=email, password=password, message=message, res=(f"thank you {name}! message on the page"))

if __name__ == '__main__':
    app.run(debug=True)