from flask import redirect, render_template, session,request, url_for

from app import app,login_required
from app.models.city import City, Company


@app.route("/add_city/", methods=["GET","POST"])
@login_required
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

@app.route("/add_company/", methods=["GET","POST"])
@login_required
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


@app.route("/city/show/<int:id>/")
@login_required
def show_city(id):
    data = {"id":id}
    city = City.get_by_id(data)
    return render_template("city/show.html", cities=city)

@app.route("/city/edit/<int:id>/", methods=["GET","POST"])
@login_required
def edit_city(id):
    if request.method == "POST":
        city = request.form["city"]
        data = {
            "city": city,
            "id": id
        }
        check = City.check_city(data)
        if check == True:
            return redirect(url_for("dashboard"))
        else:
            City.update(data)
        return redirect(url_for("dashboard"))
    city = City.get_by_id({"id":id})
    return render_template("city/edit.html", cities=city)

@app.route("/city/delete/<int:id>/")
@login_required
def delete_city(id):
    data = {"id":id}
    City.delete(data)
    return redirect(url_for("dashboard"))

@app.route("/company/show/<int:id>/")
@login_required
def show_company(id):
    data = {"id":id}
    company = Company.get_by_id(data)
    return render_template("company/show.html", companies=company)

@app.route("/company/edit/<int:id>/", methods=["GET","POST"])
@login_required
def edit_company(id):
    if request.method == "POST":
        company = request.form["company"]
        phone = request.form["phone"]
        data = {
            "company": company,
            "phone": phone,
            "id": id
        }
        
        Company.update(data)
        return redirect(url_for("dashboard"))
    company = Company.get_by_id({"id":id})
    return render_template("company/edit.html", companies=company)

@app.route("/company/delete/<int:id>/")
@login_required
def delete_company(id):
    data = {"id":id}
    Company.delete(data)
    return redirect(url_for("dashboard"))