import re
import smtplib
import phonenumbers
import json

from flask import Blueprint, render_template, request, flash, redirect, url_for

from flask_login import current_user, login_user, logout_user
from email_validator import validate_email, EmailNotValidError
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@views.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    return render_template("aboutus.html")

@views.route('/joinus', methods=['GET', 'POST'])
def joinus():
    return render_template("joinus.html")

@views.route('/concerts', methods=['GET', 'POST'])
def concerts():
    return render_template("concertsandevents.html")

@views.route('/hire', methods=['GET', 'POST'])
def hire():
    return render_template("stagesandmusichire.html")

@views.route('/members', methods=['GET', 'POST'])
def members():
    return render_template("members.html")