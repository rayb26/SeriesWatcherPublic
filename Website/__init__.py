# Code created by Rayhan Biju 2021
from flask import Flask

from os import path


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '#your secret key'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import Alert, User

    return app
