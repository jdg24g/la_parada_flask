from app import app,login_required

from flask import redirect,render_template,request,url_for,session
from app.models.city import City,Company

@app.route('/')
def index():
    return render_template('parada/index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/dashboard/")
@login_required
def dashboard():
    cities = City.get_all()
    companies = Company.get_all()
    
    return render_template("dashboard/index.html",cities=cities,companies=companies)