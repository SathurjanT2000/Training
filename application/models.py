from application import db
from datetime import datetime

class Trainers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    user_name = db.Column(db.String(40), nullable=False, unique=True)
    #password = db.binary(64), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    experience = db.Column(db.Integer, default=0)
    certificates = db.Column(db.String(30), nullable=True)

class Trainees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    PT_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    user_name = db.Column(db.String(40), nullable=False, unique=True)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    goal = db.Column(db.String(100))