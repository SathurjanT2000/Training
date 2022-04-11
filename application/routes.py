from application import app, db
from application.models import Trainers, Trainees
from application.forms import LogInForm
from flask import render_template

@app.route('/', methods=['GET','POST'])
def login():
    all_trainers = Trainers.query.all()
    all_trainees = Trainees.query.all()
    login_form = LogInForm()
    if Trainers.query.get(login_form.username.data) != None:
        return render_template('index.html', all_trainers=all_trainers, all_trainees=all_trainees, login_form=login_form)
    elif Trainees.query.get(login_form.username) != None:
        return render_template('index(trainee).html', all_trainees=all_trainees, all_trainers=all_trainers, login_form=login_form)
    else:
        return render_template('login.html', login_form=login_form)


    

