import os
from flask import Flask, render_template
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPExceptions
from werkzeug.security import check_password

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("layout.html")

if __name__=="__main__":
    app.run()
