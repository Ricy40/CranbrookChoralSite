from flask import Flask
import os
from os import path
from flask_cors import CORS

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'osdhfoidfouiyi6298273sdfkbsos2'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    CORS(app)

    return app
