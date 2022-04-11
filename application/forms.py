from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class LogInForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired()
    ])
    login = SubmitField('Log in')

class TrainersForm(FlaskForm):
    first_name = StringField('first name', validators=[
        DataRequired(),
        Length(max=30)
    ])
    last_name = StringField('last name', validators=[
        DataRequired(),
        Length(max=30)
    ])
    date_of_birth = DateField('date of birth', validators=[
        DataRequired()
    ])
    experience = IntegerField('experience')
    certificates = StringField('certificates', validators=[
        Length(max=100)
    ])
    submit = SubmitField('Add Trainer')

class TraineesForm(FlaskForm):
    first_name = StringField('first name', validators=[
        DataRequired(),
        Length(max=30)
    ])
    last_name = StringField('last name', validators=[
        DataRequired(),
        Length(max=30)
    ])
    date_of_birth = DateField('date of birth', validators=[
        DataRequired()
    ])
    goal = StringField('goal', validators=[
        Length(max=100)
    ])
    submit = SubmitField('Add Trainee')