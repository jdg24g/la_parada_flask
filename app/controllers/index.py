from app import app

from flask import redirect,render_template,request,url_for

@app.route('/')
def index():
    return render_template('parada/index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404