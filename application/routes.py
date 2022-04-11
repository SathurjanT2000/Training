from application import app, db
from application.models import Trainers, Trainees
from flask import render_template

@app.route('/')
def index():
    all_trainers = Trainers.query.all()
    all_trainees = Trainees.query.all()
    return render_template('index.html', all_trainers=all_trainers, all_trainees=all_trainees)

