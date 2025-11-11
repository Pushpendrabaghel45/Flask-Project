# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('form.html')

# @app.route('/success')
# def success():
#     return render_template('success.html')



# @app.route("/success")
# def success():
#     name = request.args.get("name")
#     email = request.args.get("email")
#     massage = request.args.get("massage")
#     return render_template("success.html", name=name, email=email, massage=massage)

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get form data
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        contact = request.form.get("contact")
        email = request.form.get("email")
        massage = request.form.get("massage")

        # password = request.form.get("password")  # Not secure for production
        
        # Simple validation
        if not firstname or not lastname or not contact or not email or not massage:
            return "All fields are required!", 400

        # Redirect to success page with data
        return redirect(url_for("success", firstname=firstname, email=email, massage= massage))
    
    return render_template("register.html")

@app.route("/success")
def success():
    firstname = request.args.get("firstname")
    email = request.args.get("email")
    massage = request.args.get("massage")
    return render_template("success.html", firstname=firstname, email=email, massage=massage)

if __name__ == "__main__":
    app.run(debug=True)
    