from flask import Flask
import os
# from flask_cors import CORS
from flask_mail import Mail

mail = Mail()

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'osdhfoidfouiyi6298273sdfkbsos2'
    app.config['MAIL_SERVER'] = os.environ.get("mail_server")
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get("mail_username")
    app.config['MAIL_PASSWORD'] = os.environ.get("mail_password")
    mail.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    # CORS(app)

    return app
