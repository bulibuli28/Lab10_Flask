from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length

class RegisterForm(FlaskForm):
    # Add Max Length to Email Field in RegisterForm 
    email = StringField('Email', description= "Your school email address", default="student@tup.edu.ph", validators=[InputRequired(), Email(), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


    email = StringField('Email', default="student@tup.edu.ph")