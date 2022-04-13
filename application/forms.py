from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class LogInForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired()
    ])
    login = SubmitField('Log in')

class TrainersForm(FlaskForm):
    first_name = StringField('First name', validators=[
        DataRequired(),
        Length(max=30)
    ])
    last_name = StringField('Last name', validators=[
        DataRequired(),
        Length(max=30)
    ])
    date_of_birth = DateField('Date of birth', validators=[
        DataRequired()
    ])
    experience = IntegerField('Experience')
    certificates = StringField('Certificates', validators=[
        Length(max=100)
    ])
    register = SubmitField('Add Trainer')

class TraineesForm(FlaskForm):
    first_name = StringField('First name', validators=[
        DataRequired(),
        Length(max=30)
    ])
    last_name = StringField('Last name', validators=[
        DataRequired(),
        Length(max=30)
    ])
    date_of_birth = DateField('Date of birth', validators=[
        DataRequired()
    ])
    goal = StringField('Goal', validators=[
        Length(max=100)
    ])
    register = SubmitField('Add Trainee')