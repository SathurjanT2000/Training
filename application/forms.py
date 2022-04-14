from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from datetime import datetime, timedelta

#Checks to see if the field contains only alphabets.
class CharactersCheck:
    def __init__(self, message=None):
        if not message:
            message = "Invalid name, please remove special characters and numbers" #currently not testable
        self.message = message
    
    def __call__(self, form, field):
        if field.data.isalpha() == False:
            raise ValidationError(self.message)

#Checks to see if the person is old enough to be a trainer or trainee or too old to be either.
class AgeCheck:
    def __init__(self, number, message=None):#number is the age restriction e.g. only people over 18 can be trainers
        self.number = number
        if not message:
            message = "Invalid date, please pick another date"
        self.message = message

    def __call__(self, form, field):
        if field.data > datetime.date(datetime.now()):
            raise ValidationError(self.message)
        elif datetime.date(datetime.now()) - field.data < timedelta(self.number*365):
            raise ValidationError(self.message)
        elif datetime.date(datetime.now()) - field.data > timedelta(100*365):
            raise ValidationError(self.message)

#checks to see if the field contains any of the given characters in the "not_allowed"
class NotAllowedCharacters:
    def __init__(self, not_allowed, message=None):
        self.not_allowed = not_allowed
        if not message:
            message = f"Invalid characters, please don't use any of these characters: {self.not_allowed} or numbers"
        self.message = message
    
    def __call__(self, form, field):
        for char in field.data:
            if char in self.not_allowed or char.isdigit() == True:
                raise ValidationError(self.message)
                break

#Log in form used at index
class LogInForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired()
    ])
    login = SubmitField('Log in')

#Registering form used at idex for trainers
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
 
#Registering form used at trainer_home for trainees
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
        NotAllowedCharacters(not_allowed = '!#%&?\\/"\'$£')
    ])
    register = SubmitField('Add Trainee')
    
#Update form used at update page to change a trainee's goal
class UpdateForm(FlaskForm):
    goal = StringField('Goal', validators=[
        Length(max=100),
        NotAllowedCharacters(not_allowed = '!#%&?\\/"\'$£')
    ])
    update = SubmitField('Update goal')