from app import app

from flask import redirect,render_template,request,url_for

@app.route('/')
def index():
    return render_template('parada/index.html')