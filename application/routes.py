from application import app, db
from application.models import Trainers, Trainees
from application.forms import LogInForm, TrainersForm
from flask import render_template, request, redirect, url_for

@app.route('/', methods=['GET','POST'])
def index():
    login_form = LogInForm()
    trainers_form = TrainersForm()

    if Trainers.query.filter_by(user_name=login_form.username.data).first() != None:
        return redirect(url_for('home_trainer'), code=302)
    elif Trainees.query.filter_by(user_name=login_form.username.data).first() != None:
        return redirect(url_for('home_trainee'), code=302)
    else:
        try: 
            if request.method == "POST":
                task = Trainers(
                    first_name = trainers_form.first_name.data,
                    last_name = trainers_form.last_name.data,
                    date_of_birth = trainers_form.date_of_birth.data,
                    experience = trainers_form.experience.data,
                    certificates = trainers_form.certificates.data,
                    user_name = str(trainers_form.date_of_birth.data)[-2:] + trainers_form.first_name.data + trainers_form.last_name.data
                )
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('home_trainer', code=302))
        except:
            return render_template('index.html', login_form=login_form, trainers_form=trainers_form)
          
@app.route('/home_trainee')
def home_trainee():
    return render_template('trainee_home.html')

@app.route('/home_trainer')
def home_trainer():
    return render_template('trainer_home.html')
