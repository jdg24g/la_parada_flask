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


@app.route("/register/", methods=["POST"])
def register():
    first_name = request.form["first_name"]
    print(first_name)
    last_name = request.form["last_name"]
    print(last_name)
    email = request.form["email"]
    print(email)
    password = request.form["password"]
    print(password)
    comfirm_password = request.form["confirm_password"]
    print(comfirm_password)
    # All fields must not be empty
    if not first_name or not last_name or not email or not password or not comfirm_password:
        print("empty fields")
        return redirect(url_for("admin"))
    # email must be valid
    if not valid_email(email):
        print("invalid email")
        return redirect(url_for("admin"))
    # password must be at least 8 characters
    if len(password) < 8:
        print("password too short")
        return redirect(url_for("admin"))
    # password and confirm password must match
    if password != comfirm_password:
        print("passwords do not match")
        return redirect(url_for("admin"))
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
        data = {"email": email}
        user = User.get_by_email(data)
        if user == None:
            print("user is none")
            return redirect(url_for("admin"))
        # check if email exists in database
        # check if password is correct

        if email == user.email and bcrypt.check_password_hash(user.password, password):
            session["user"] = {
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
    # user in session redirect to dashboard
    if "user" in session:
        return redirect(url_for("dashboard"))

    return render_template("auth/index.html")
