from flask import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import DateField, TimeField
from final_year.models import User, Appointment

class RegistrationForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired(), Length(min=8, max=120)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username taken')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email taken')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AppointmentForm(FlaskForm):
    fullname = StringField('Full name', validators=[DataRequired()])
    phone_number = StringField('Phone number', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired()])
    reason = StringField('Reason', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    
    