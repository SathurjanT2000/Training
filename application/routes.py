from application import app, db
from application.models import Trainers, Trainees
from application.forms import LogInForm, TrainersForm, TraineesForm, UpdateForm
from flask import render_template, request, redirect, url_for

@app.route('/', methods=['GET','POST'])
def index():
    login_form = LogInForm()
    trainers_form = TrainersForm()

    if Trainers.query.filter_by(user_name=login_form.username.data).first() != None:
        name = Trainers.query.filter_by(user_name=login_form.username.data).first().last_name
        Pt_id = Trainers.query.filter_by(user_name=login_form.username.data).first().id
        return redirect(url_for('home_trainer', name=name, Pt_id=Pt_id))
    elif Trainees.query.filter_by(user_name=login_form.username.data).first() != None:
        name = Trainees.query.filter_by(user_name=login_form.username.data).first().last_name
        t_id = Trainees.query.filter_by(user_name=login_form.username.data).first().id
        return redirect(url_for('home_trainee', name=name, t_id=t_id))
    else:
        try: 
            if request.method == "POST":
                trainer = Trainers(
                    first_name = trainers_form.first_name.data,
                    last_name = trainers_form.last_name.data,
                    date_of_birth = trainers_form.date_of_birth.data,
                    experience = trainers_form.experience.data,
                    certificates = trainers_form.certificates.data,
                    user_name = str(trainers_form.date_of_birth.data)[-2:] + trainers_form.first_name.data + trainers_form.last_name.data
                )
            db.session.add(trainer)
            db.session.commit()
            name = trainers_form.last_name.data
            Pt_id = trainer.id
            return redirect(url_for('home_trainer', name=name, Pt_id=Pt_id))
        except:
            return render_template('index.html', login_form=login_form, trainers_form=trainers_form)
          
@app.route('/home_trainee')
def home_trainee():
    name = request.args.get('name')
    t_id = request.args.get('t_id')
    goal = Trainees.query.get(t_id).goal
    Pt_id = Trainees.query.get(t_id).PT_id
    Pt_name = Trainers.query.get(Pt_id).first_name + " " + Trainers.query.get(Pt_id).last_name
    Pt_experience = Trainers.query.get(Pt_id).experience
    Pt_certificates = Trainers.query.get(Pt_id).certificates
    return render_template('trainee_home.html', name=name, Pt_certificates=Pt_certificates, Pt_experience=Pt_experience, Pt_name=Pt_name, goal=goal)

@app.route('/home_trainer', methods=['GET', 'POST'])
def home_trainer():
    all_trainees = Trainees.query.all()
    trainees_form = TraineesForm()
    name = request.args.get('name')
    Pt_id = request.args.get('Pt_id')
    if request.method == "POST":
        trainee = Trainees(
            PT_id = Pt_id,
            first_name = trainees_form.first_name.data,
            last_name = trainees_form.last_name.data,
            user_name = str(trainees_form.date_of_birth.data)[-2:] + trainees_form.first_name.data + trainees_form.last_name.data,
            date_of_birth = trainees_form.date_of_birth.data,
            goal = trainees_form.goal.data
        )
        db.session.add(trainee)
        db.session.commit()
        return redirect(url_for('home_trainer', name=name, trainees_form=trainees_form, Pt_id=Pt_id, all_trainees=all_trainees))
    return render_template('trainer_home.html', name=name, trainees_form=trainees_form, Pt_id=Pt_id, all_trainees=all_trainees)

@app.route('/delete/<int:id>')
def delete_trainee(id):
    name = request.args.get('name')
    Pt_id = request.args.get('Pt_id')
    trainee = Trainees.query.get(id)
    db.session.delete(trainee)
    db.session.commit()
    return redirect(url_for('home_trainer', name=name, Pt_id=Pt_id))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_trainee(id):
    name = request.args.get('name')
    Pt_id = request.args.get('Pt_id')
    updateform = UpdateForm()
    trainee = Trainees.query.get(id)

    if request.method == "POST":
        trainee.goal = updateform.goal.data
        db.session.commit()
        return redirect(url_for('home_trainer', name=name, Pt_id=Pt_id))
    return render_template('update.html', updateform=updateform)