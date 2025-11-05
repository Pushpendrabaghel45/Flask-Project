from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for CSRF protection

# ---- Contact Form ----
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=5)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=5)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Submit')

# ---- Routes ----
@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        return render_template('contact.html', form=form, success=True, name=name)
    return render_template('contact.html', form=form, success=False)

if __name__ == '__main__':
    app.run(debug=True)
