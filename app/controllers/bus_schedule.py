from flask import redirect, render_template, request, session, url_for
from app import app, login_required
from app.models.city import City,Company
from app.models.bus_schedule import Schedule



@app.route("/add_bus_schedule/", methods=["GET", "POST"])
@login_required
def add_bus_schedule():
    cities = City.get_all()
    companies = Company.get_all()
    if request.method == "POST":
        company_id = request.form["company_id"]
        print(company_id)
        
        schedule = request.form["schedule"]
        print(schedule)
        city_id = request.form["city_id"]
        print(city_id)
        
        data ={
            "company_id": company_id,
            "city_id": city_id,
            "schedule": schedule
        }
        print(data)
        Schedule.create(data)
        return redirect(url_for("add_bus_schedule"))
    return render_template("bus_schedule/index.html", companies=companies,cities=cities)

