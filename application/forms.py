from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from datetime import datetime, timedelta

class CharactersCheck:
    def __init__(self, message=None):
        if not message:
            message = "Invalid name, please remove special characters and numbers"
        self.message = message
    
    def __call__(self, form, field):
        if field.data.isalpha() == False:
            raise ValidationError(self.message)

class AgeCheck:
    def __init__(self, number, message=None):
        self.number = number
        if not message:
            message = "Invalid date, please pick another date"
        self.message = message

    def __call__(self, form, field):
        if field.data > datetime.date(datetime.now()):
            raise ValidationError(self.message)
        elif datetime.date(datetime.now()) - field.data < timedelta(self.number*365):
            raise ValidationError(self.message)

class LogInForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired()
    ])
    login = SubmitField('Log in')

class TrainersForm(FlaskForm):
    first_name = StringField('First name', validators=[
        DataRequired(),
        Length(max=30),
        CharactersCheck(message="Invalid First name, please remove special characters and numbers")
    ])
    
    last_name = StringField('Last name', validators=[
        DataRequired(),
        Length(max=30),
        CharactersCheck(message="Invalid Last name, please remove special characters and numbers")
    ])

    date_of_birth = DateField('Date of birth', validators=[
        DataRequired(),
        AgeCheck(number=18)
    ])
    experience = IntegerField('Experience', validators=[
        NumberRange(min=0, max=50)
    ])
    certificates = StringField('Certificates', validators=[
        Length(max=100)
    ])
    register = SubmitField('Add Trainer')
 
class TraineesForm(FlaskForm):
    first_name = StringField('First name', validators=[
        DataRequired(),
        Length(max=30),
        CharactersCheck(message="Invalid First name, please remove special characters and numbers")
    ])
    last_name = StringField('Last name', validators=[
        DataRequired(),
        Length(max=30),
        CharactersCheck(message="Invalid Last name, please remove special characters and numbers")
    ])
    date_of_birth = DateField('Date of birth', validators=[
        DataRequired(),
        AgeCheck(number=10)
    ])
    goal = StringField('Goal', validators=[
        Length(max=100),
        CharactersCheck(message="Invalid goal, please remove special characters and numbers")
    ])
    register = SubmitField('Add Trainee')
    
class UpdateForm(FlaskForm):
    goal = StringField('Goal', validators=[
        Length(max=100),
        CharactersCheck(message="Invalid goal, please remove special characters and numbers")
    ])
    update = SubmitField('Update goal')