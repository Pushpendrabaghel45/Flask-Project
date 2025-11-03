from flask import Flask, render_template

app = Flask(__name__)




@app.route("/")
def home():
    return render_template('Home.html')

@app.route("/about")
def about():
    return render_template('About.html')

@app.route("/contact")
def contact():
    return render_template('Contact.html')

@app.route("/index")
def index():
    return render_template('index.html')



if __name__ == "__main__":
     app.run(debug=True)

# @app.route("/user/<name>")
# def greet_user(name):
#     return f"Hello, {name}!"



