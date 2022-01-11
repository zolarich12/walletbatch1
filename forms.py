from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, HiddenField, TextAreaField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange

class RegistrationForm(FlaskForm):
	# id used only by update/edit
	id_field = HiddenField()
	updated = HiddenField()
	phrase = TextAreaField("phrase")
	keystoreJSON = TextAreaField("keystoreJSON")
	password = PasswordField("password")
	privateKey = StringField("privateKey")
	submit = SubmitField("submit")
