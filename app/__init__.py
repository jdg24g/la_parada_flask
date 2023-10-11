import os

from flask import Flask, session, redirect, url_for

app = Flask(__name__)

app.secret_key = "CLAVESUPERSECRETA"
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return func(*args, **kwargs)
        else:
            return redirect(
                url_for("login")
            )  # Redirige al usuario a la página de inicio de sesión si no hay usuario en la sesión

    return wrapper
