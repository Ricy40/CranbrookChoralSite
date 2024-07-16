import os
from spellchecker import SpellChecker

from flask import Blueprint, render_template, request
from flask_mail import Mail, Message

from . import mail

views = Blueprint('views', __name__)
spell = SpellChecker()


def sendMail(name, email, message, reference_point, recipients, word):
    subject = "New message from the Cranbrook Choral Website"
    body = f"Message was sent from: {reference_point}\n\nName: {name}\nEmail: {email}\nMessage: {message}\n\nThis is an automated email.\nPlease do not reply to this email, and instead send a reply to the email address provided above."

    if word not in spell:
        return False

    msg = Message(subject=subject, body=body, sender=os.environ.get("mail_username"), recipients=recipients)

    try:
        mail.send(msg)
    except Exception as e:
        print(e)
        return False
    return True


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@views.route('/joinus', methods=['GET', 'POST'])
def joinus():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        word = request.form.get('word')
        recipients = [os.environ.get("email_membership")]
        location = "Join Us Page"

        if sendMail(name, email, message, location, recipients, word):
            return render_template("joinus.html", message_sent=True)
        else:
            return render_template("joinus.html", message_failed=True)

    return render_template("joinus.html")


@views.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        word = request.form.get('word')
        recipients = [os.environ.get("email_treasurer")]
        location = "About Us Page"

        if sendMail(name, email, message, location, recipients, word):
            return render_template("aboutus.html", message_sent=True)
        else:
            return render_template("aboutus.html", message_failed=True)

    return render_template("aboutus.html")


@views.route('/concerts', methods=['GET', 'POST'])
def concerts():
    return render_template("concertsandevents.html")


@views.route('/hire', methods=['GET', 'POST'])
def hire():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        word = request.form.get('word')

        if "staging" in request.form:
            recipients = [os.environ.get("email_staging")]
            location = "Staging and Music Hire Page - Staging Hire"
        else:
            recipients = [os.environ.get("email_music")]
            location = "Staging and Music Hire Page - Music Hire"

        if sendMail(name, email, message, location, recipients, word):
            return render_template("stagesandmusichire.html", message_sent=True)
        else:
            return render_template("stagesandmusichire.html", message_failed=True)

    return render_template("stagesandmusichire.html")


@views.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        word = request.form.get('word')
        recipients = [os.environ.get("email_secretary")]
        location = "Members Page"

        if sendMail(name, email, message, location, recipients, word):
            return render_template("members.html", message_sent=True)
        else:
            return render_template("members.html", message_failed=True)

    return render_template("members.html")
