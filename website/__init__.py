from flask import Flask
import os
from flask_mail import Mail

mail = Mail()

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get("secret_key")
    app.config['MAIL_SERVER'] = os.environ.get("mail_server")
    app.config['MAIL_PORT'] = os.environ.get("mail_port")
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = os.environ.get("mail_username")
    app.config['MAIL_PASSWORD'] = os.environ.get("mail_password")
    mail.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
