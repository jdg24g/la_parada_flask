from flask import redirect, render_template, session, url_for

from app import app
from app.models.city import City, Company
from flask import request


@app.route("/add_city", methods=["GET","POST"])
def add_city():
    if request.method == "POST":
        city = request.form["city"]
        #city no empety and city no repeate
        if not city:
            return redirect(url_for("dashboard"))
        data = {
            "city": city
        }
        #check if city exist
        check = City.check_city(data)
        print(check)

        if check == True:
            return redirect(url_for("dashboard"))
        else:
            City.create(data)
    return redirect(url_for("dashboard"))

@app.route("/add_company", methods=["GET","POST"])
def add_company():
    if request.method == "POST":
        company = request.form["company"]
        phone = request.form["phone"]
        if not company:
            return redirect(url_for("dashboard"))
        data = {
            "company": company,
            "phone": phone
        }
        check = Company.check_company(data)
        if check == True:
            print("company exist")
            return redirect(url_for("dashboard"))
        else:
            print("company no exist")
            Company.create(data)

    return redirect(url_for("dashboard"))


@app.route("/city/show/<int:id>")
def show_city(id):
    data = {"id":id}
    city = City.get_by_id(data)
    return render_template("city/show.html", cities=city)

@app.route("/city/edit/<int:id>", methods=["GET","POST"])
def edit_city(id):
    if request.method == "POST":
        city = request.form["city"]
        phone = request.form["phone"]
        data = {
            "city": city,
            "phone": phone,
            "id": id
        }
        City.update(data)
        return redirect(url_for("dashboard"))
    city = City.get_by_id({"id":id})
    return render_template("city/edit.html", cities=city)