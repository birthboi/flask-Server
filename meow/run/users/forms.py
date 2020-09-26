from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from run.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)]) # Username input
	email = StringField('Email', validators=[DataRequired(), Email()]) # Email input
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8)]) # Password - Confirm Password = Password Inputs
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

	submit = SubmitField('Sign Up')

	def validate_username(self, username):

		user = User.query.filter_by(username=username.data).first()

		if user:
			raise ValidationError(f'That username is taken! Please choose a different one (e.g. {username.data}123, xx{username.data}xx).')

	def validate_email(self, email):

		user = User.query.filter_by(email=email.data).first()

		if user:
			raise ValidationError(f'That email is taken! Please choose a different one.')



class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()]) # Email input
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8)]) # Password - Confirm Password = Password Inputs

	remember = BooleanField('Remember Me!')

	submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)]) # Username input
	email = StringField('Email', validators=[DataRequired(), Email()]) # Email input

	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'bmp'])])

	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()

			if user:
				raise ValidationError(f'That username is taken! Please choose a different one (e.g. {username.data}123, xx{username.data}xx).')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()

			if user:
				raise ValidationError(f'That email is taken! Please choose a different one.')
