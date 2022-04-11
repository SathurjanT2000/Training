from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PositiveIntegerField, SubmitField
from wtforms.validators import DataRequired, Length

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
    experience = PositiveIntegerField('experience', validators=[
        default=100,
        max_digits=2
    ])
    certificates = StringField('certificates', validators=[
        Length(max=100)
    ])
    submit = SubmitField('Add Trainer')

