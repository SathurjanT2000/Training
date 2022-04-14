from application import app, db
from application.models import Trainers, Trainees
from application.forms import LogInForm, TrainersForm, TraineesForm, UpdateForm
from flask import render_template, request, redirect, url_for

@app.route('/', methods=['GET','POST'])
def index():
    login_form = LogInForm()
    trainers_form = TrainersForm()

    if Trainers.query.filter_by(user_name=login_form.username.data).first() != None: #checks to see if the given username belongs in the Trainers table in the db
        name = Trainers.query.filter_by(user_name=login_form.username.data).first().last_name #to send it to other pages
        Pt_id = Trainers.query.filter_by(user_name=login_form.username.data).first().id
        return redirect(url_for('home_trainer', name=name, Pt_id=Pt_id))
    elif Trainees.query.filter_by(user_name=login_form.username.data).first() != None: #checks to see if the given username belongs in the Trainees table in the db
        name = Trainees.query.filter_by(user_name=login_form.username.data).first().last_name #to send it to other pages
        t_id = Trainees.query.filter_by(user_name=login_form.username.data).first().id
        return redirect(url_for('home_trainee', name=name, t_id=t_id))
    else: #the bit for registering trainers
        if trainers_form.validate_on_submit():
            trainer = Trainers(
                first_name = trainers_form.first_name.data,
                last_name = trainers_form.last_name.data,
                date_of_birth = trainers_form.date_of_birth.data,
                experience = trainers_form.experience.data,
                certificates = trainers_form.certificates.data,
                user_name = str(trainers_form.date_of_birth.data)[-2:] + trainers_form.first_name.data + trainers_form.last_name.data #creating username, it will store day of birth + fullname
            )
            db.session.add(trainer)
            db.session.commit()
            name = trainers_form.last_name.data#to sent it to other pages
            Pt_id = trainer.id
            return redirect(url_for('home_trainer', name=name, Pt_id=Pt_id))
    return render_template('index.html', login_form=login_form, trainers_form=trainers_form)
          
@app.route('/home_trainee')
def home_trainee():
    name = request.args.get('name') #pulling the given data from other pages
    t_id = request.args.get('t_id')
    goal = Trainees.query.get(t_id).goal #to send it to other pages
    Pt_id = Trainees.query.get(t_id).PT_id
    Pt_name = Trainers.query.get(Pt_id).first_name + " " + Trainers.query.get(Pt_id).last_name #just building the trainer's fullname
    Pt_experience = Trainers.query.get(Pt_id).experience
    Pt_certificates = Trainers.query.get(Pt_id).certificates
    return render_template('trainee_home.html', name=name, Pt_certificates=Pt_certificates, Pt_experience=Pt_experience, Pt_name=Pt_name, goal=goal)

@app.route('/home_trainer', methods=['GET', 'POST'])
def home_trainer():
    all_trainees = Trainees.query.all() #getting data from db
    trainees_form = TraineesForm()
    name = request.args.get('name') #pulling the given data from other pages
    Pt_id = request.args.get('Pt_id')
    if trainees_form.validate_on_submit(): #the bit for registering trainees
        trainee = Trainees(
            PT_id = Pt_id,
            first_name = trainees_form.first_name.data,
            last_name = trainees_form.last_name.data,
            user_name = str(trainees_form.date_of_birth.data)[-2:] + trainees_form.first_name.data + trainees_form.last_name.data, #same username building
            date_of_birth = trainees_form.date_of_birth.data,
            goal = trainees_form.goal.data
        )
        db.session.add(trainee)
        db.session.commit()
        return redirect(url_for('home_trainer', name=name, trainees_form=trainees_form, Pt_id=Pt_id, all_trainees=all_trainees))
    return render_template('trainer_home.html', name=name, trainees_form=trainees_form, Pt_id=Pt_id, all_trainees=all_trainees)

@app.route('/delete/<int:id>') 
def delete_trainee(id):
    name = request.args.get('name') #pulling data
    Pt_id = request.args.get('Pt_id')
    trainee = Trainees.query.get(id) #getting trainee based on id
    db.session.delete(trainee)
    db.session.commit()
    return redirect(url_for('home_trainer', name=name, Pt_id=Pt_id))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_trainee(id):
    name = request.args.get('name') #pulling data
    Pt_id = request.args.get('Pt_id')
    updateform = UpdateForm()
    trainee = Trainees.query.get(id)

    if updateform.validate_on_submit():
        trainee.goal = updateform.goal.data
        db.session.commit()
        return redirect(url_for('home_trainer', name=name, Pt_id=Pt_id))
    return render_template('update.html', updateform=updateform)