from application import app, db
from application.models import Trainers, Trainees
from application.forms import LogInForm
from flask import render_template

@app.route('/', methods=['GET','POST'])
def index():
    all_trainers = Trainers.query.all()
    all_trainees = Trainees.query.all()
    login_form = LogInForm()
    if Trainers.query.filter_by(user_name=login_form.username.data).first() != None:
        return render_template('trainer_home.html', all_trainers=all_trainers, all_trainees=all_trainees, login_form=login_form)
    elif Trainees.query.filter_by(user_name=login_form.username.data).first() != None:
        return render_template('trainee_home.html', all_trainees=all_trainees, all_trainers=all_trainers, login_form=login_form)
    else:
        return render_template('index.html', login_form=login_form, all_trainees=all_trainees, all_trainers=all_trainers)


@app.route('/home_trainee')
def home_trainee():
    return render_template('trainee_home.html')

@app.route('/home_trainer')
def home_trainer():
    return render_template('trainer_home.html')
