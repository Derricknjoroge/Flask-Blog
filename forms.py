from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, Length, DataRequired, EqualTo, ValidationError


class Register(FlaskForm):
    '''This is a class that creates the register form'''
    username = StringField('Username', validators=[Length(min=5, max=10), DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=12)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class Login(FlaskForm):
    '''This is a class that creates the login form'''
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=12)])
    submit = SubmitField('Sign In')