from flask_testing import TestCase
from application import app, db
from application.models import Trainees, Trainers
from application.forms import LogInForm
from flask import url_for
import uuid

class TestBase(TestCase):
    def create_app(self):
        try:
            from Secrets import SQLALCHEMY_TEST_DATABASE_URI
            app.config.update(
                SQLALCHEMY_DATABASE_URI= SQLALCHEMY_TEST_DATABASE_URI,
                SECRET_KEY = str(uuid.uuid4),
                WTF_CSRF_ENABLED=False
            )
            return app
        except:
            from os import getenv
            app.config.update(
                SQLALCHEMY_DATABASE_URI= getenv("SQLALCHEMY_DATABASE_URI"),
                SECRET_KEY = str(uuid.uuid4),
                WTF_CSRF_ENABLED=False
            )
            return app

    def setUp(self):
        db.create_all()
     
        Marc = Trainers(first_name="Marc", last_name="Spencer", user_name="Marc", date_of_birth="1000-4-3", experience=3, certificates="mer")
        Sam = Trainees(PT_id=1, first_name="Sam", last_name="kev", user_name="Sam", date_of_birth="2022-03-03", goal="meg")
      
        db.session.add(Marc)
        db.session.commit()
        db.session.add(Sam)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class testViews(TestBase):
    #very first test, simply testing to see if a connection has been successfully made
    def test_login_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

class testAccess(TestBase):
    #testing to see if log in system works for trainers
    def test_trainer(self): 
        response = self.client.post(
            url_for('index'), data = dict(username="Marc"), follow_redirects=True
        )
        self.assertIn(b'Welcome, Trainer Spencer', response.data)

    def test_trainee(self):
        #testing to see if log in system works for trainees
        response = self.client.post(
            url_for('index'), data = dict(username="Sam"), follow_redirects=True
        )
        self.assertIn(b'Welcome, Trainee Kev', response.data)

    def test_register_trainer(self):
        #testing to see if registering trainers work
        response = self.client.post(
            url_for('index'), data = dict(
                first_name = "May",
                last_name = "Summer",
                date_of_birth = "2000-04-03",
                experience = 3,
                certificates = "hello"
            ),
            follow_redirects=True
        )
        self.assertIn(b'Welcome, Trainer Summer', response.data)

    def test_register_trainee(self):
        #testing to see if registering trainees work
        response = self.client.post(
            url_for('home_trainer', Pt_id=1, name="hello"), data = dict(
                first_name = "May",
                last_name = "winter",
                date_of_birth = "2000-04-03",
                goal = 'meh'
            ),
            follow_redirects=True
        )
        self.assertIn(b'May winter', response.data)

    #Validation checks

    def test_register_trainer_validation(self):
        #number and space input in names are checked
        #age check is performed
        #out of range experience is checked
        response = self.client.post(
            url_for('index'), data = dict(
                first_name = "May1",
                last_name = "Sum mer",
                date_of_birth = "2020-04-03",
                experience = 400,
                certificates = "hello"
            ),
            follow_redirects=True
        )
        self.assertIn(b'Invalid First name, please remove special characters and numbers', response.data)
        self.assertIn(b'Invalid Last name, please remove special characters and numbers', response.data)
        self.assertIn(b'Invalid date, please pick another date', response.data)
        self.assertIn(b'Number must be between 0 and 50.', response.data)

    def test_register_trainer_validation_1(self):
        #special character input in names is checked
        #name exceeding limit is checked
        #lower boundary is checked for experience
        #future date is checked
        response = self.client.post(
            url_for('index'), data = dict(
                first_name = "May$",
                last_name = "Summerdkfokmsfmokdmkmfksmkmfkmmoksmfsdkmsmkmfmksdfkmsmfkosf",
                date_of_birth = "2030-04-03",
                experience = 0,
                certificates = "hello"
            ),
            follow_redirects=True
        )
        self.assertIn(b'Invalid First name, please remove special characters and numbers', response.data)
        self.assertIn(b'Field cannot be longer than 30 characters', response.data)
        self.assertIn(b'Invalid date, please pick another date', response.data)
        self.assertNotIn(b'Number must be between 0 and 50.', response.data)

    def test_register_trainer_validation_2(self):
        #upper limit for experience is checked
        response = self.client.post(
            url_for('index'), data = dict(
                first_name = "May$",
                last_name = "Sum_mer",
                date_of_birth = "2030-04-03",
                experience = 50,
                certificates = "hello"
            ),
            follow_redirects=True
        )
        self.assertIn(b'Invalid First name, please remove special characters and numbers', response.data)
        self.assertIn(b'Invalid Last name, please remove special characters and numbers', response.data)
        self.assertIn(b'Invalid date, please pick another date', response.data)
        self.assertNotIn(b'Number must be between 0 and 50.', response.data)

    def test_register_trainee_validation(self):
        #very old date is checked
        #special characters in goal is checked
        response = self.client.post(
            url_for('home_trainer', Pt_id=1, name="hello"), data = dict(
                first_name = "Ma y",
                last_name = "win4ter",
                date_of_birth = "1000-04-03",
                goal = 'me%h'
            ),
            follow_redirects=True
        )
        self.assertIn(b'Invalid First name, please remove special characters and numbers', response.data)
        self.assertIn(b'Invalid Last name, please remove special characters and numbers', response.data)
        self.assertIn(b'Invalid date, please pick another date', response.data)
        self.assertIn(b'Invalid characters, please don\'t use any of these characters:', response.data)


    def test_register_trainee_validation_1(self):
        #numbers in goal is checked
        response = self.client.post(
            url_for('home_trainer', Pt_id=1, name="hello"), data = dict(
                first_name = "Ma4y",
                last_name = "win$ter",
                date_of_birth = "1000-04-03",
                goal = 'me4h'
            ),
            follow_redirects=True
        )
        self.assertIn(b'Invalid First name, please remove special characters and numbers', response.data)
        self.assertIn(b'Invalid Last name, please remove special characters and numbers', response.data)
        self.assertIn(b'Invalid date, please pick another date', response.data)
        self.assertIn(b'Invalid characters, please don\'t use any of these characters:', response.data)

class testData(TestBase):
    #testing to see if trainee details are displayed on trainer home page
    def test_data_on_trainers_home(self):
        response = self.client.post(
            url_for('home_trainer', Pt_id=1, name="Spencer"), data = dict(
                first_name = "Summer",
                last_name = "Paige",
                date_of_birth = "2000-04-03",
                goal = 'meh'
            ),
            follow_redirects=True
        )
        self.assertIn(b'Welcome, Trainer Spencer', response.data)
        self.assertIn(b'Summer Paige', response.data)
        self.assertIn(b'03SummerPaige', response.data)
        self.assertIn(b'meh', response.data)

    def test_data_on_trainees_home(self):
        #testing to see if trainer details and goal are displayed on trainee home page
        response = self.client.post(
            url_for('index', name="kev", t_id=1), data = dict(username="Sam"), follow_redirects=True
        )
        self.assertIn(b'Welcome, Trainee Kev', response.data)
        self.assertIn(b'Marc Spencer', response.data)
        self.assertIn(b'3 years', response.data)
        self.assertIn(b'Meg', response.data) #certificates
        self.assertIn(b'Mer', response.data) #goal

class testChange(TestBase):
    #testing to see if trianee is removed
    def test_delete(self):
        response = self.client.get(
            url_for('delete_trainee', id=1, name="Marc Spencer", Pt_id=1), follow_redirects=True
        )
        self.assertNotIn(b'Sam kev', response.data)

    def test_update(self):
        #testing to see if goal is removed
        response = self.client.post(
            url_for('update_trainee', id=1, name="Marc Spencer", Pt_id=1), data = dict(goal="Testing_update"), follow_redirects=True
        )
        self.assertIn(b'Testing_update', response.data)
        self.assertNotIn(b'Meg', response.data)

    #Validation checks
    #special characters are checked
    def test_update_validation_check(self):
        response = self.client.post(
            url_for('update_trainee', id=1, name="Marc Spencer", Pt_id=1), data = dict(goal="Testing£update"), follow_redirects=True
        )
        self.assertIn(b'Invalid characters, please don\'t use any of these characters:', response.data)

