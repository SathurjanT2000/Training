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
    def test_login_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

class testAccess(TestBase):
    def test_trainer(self): 
        response = self.client.post(
            url_for('index'), data = dict(username="Marc"), follow_redirects=True
        )
        self.assertIn(b'Welcome, Trainer Spencer', response.data)

    def test_trainee(self):
        response = self.client.post(
            url_for('index'), data = dict(username="Sam"), follow_redirects=True
        )
        self.assertIn(b'Welcome, Trainee Kev', response.data)

    def test_register_trainer(self):
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
                
class testData(TestBase):
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
        response = self.client.post(
            url_for('index', name="kev", t_id=1), data = dict(username="Sam"), follow_redirects=True
        )
        self.assertIn(b'Welcome, Trainee Kev', response.data)
        self.assertIn(b'Marc Spencer', response.data)
        self.assertIn(b'3 years', response.data)
        self.assertIn(b'Meg', response.data)
        self.assertIn(b'Mer', response.data)

class testChange(TestBase):
    def test_delete(self):
        response = self.client.post(
            url_for('delete_trainee', id=1, name="Marc Spencer", Pt_id=1), follow_redirects=True
        )
        self.assertNotIn(b'Sam kev', response.data)
