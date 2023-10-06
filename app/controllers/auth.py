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