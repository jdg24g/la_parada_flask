import re

from flask import redirect, render_template, request, session, url_for
from flask_bcrypt import Bcrypt

from app import app
from app.models.user import User

bcrypt = Bcrypt(app)

regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")


def valid_email(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        comfirm_password = request.form["confirm_password"]

        # All fields must not be empty
        if (
            not first_name
            or not last_name
            or not email
            or not password
            or not comfirm_password
        ):
            return url_for("index")
        # email must be valid
        if not valid_email(email):
            return url_for("index")
        # password must be at least 8 characters
        if len(password) < 8:
            return url_for("index")
        # password and confirm password must match
        if password != comfirm_password:
            return url_for("index")

        # hash password
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        # create user data
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": hashed_password,
        }
        print(data)
        # insert user data into database
        User.create(data)

    return redirect(url_for("admin"))


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        # check if email exists in database
        data = {"email": email}
        user = User.get_by_email(data)
        print(user.first_name)
        # check if password is correct
        if user == None:
            return redirect(url_for("admin"))
        if email == user.email and bcrypt.check_password_hash(user.password, password):
            session['user'] = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            }
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("admin"))
    return redirect(url_for("admin"))


@app.route("/logout/")
def logout():
    if "user" not in session:
        return redirect(url_for("index"))
    session.clear()
    return redirect(url_for("index"))

@app.route("/admin/")
def admin():
    #user in session redirect to dashboard
    if "user" in session:
        return redirect(url_for("dashboard"))
    
    return render_template("auth/index.html")


@app.route("/dashboard/")
def dashboard():
    if "user" not in session:
        return redirect(url_for("admin"))
    return render_template("dashboard/index.html")