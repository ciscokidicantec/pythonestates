from flask_wtf import FlaskForm
from wtforms import StringField, PassworldField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                validators=[DataRequired(),
                Length(min=2, max=50)])
    email = StringField('Email',
                validators=[DataRequired(), Email()])       
    password = PassworldField('Password',
                validators=[DataRequired()])
    confirm_password = PassworldField('Confirm Password',
                validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired(), Email()])       
    password = PassworldField('Password',
                validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
