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
     
        Marc = Trainers(first_name="Marc", last_name="Spencer", user_name="Marc", date_of_birth="1000-4-3")
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
        with self.client:
            response = self.client.post(
                url_for('index'), data = dict(username="Marc"), follow_redirects=True
            )
            self.assertIn(b'hi i am a trainer', response.data)

    def test_trainee(self):
        print("i am being triggered")
        with self.client:
            response = self.client.post(
                url_for('index'), data = dict(username="Sam"), follow_redirects=True
            )
            self.assertIn(b'hi i am a trainee', response.data)

    def test_register_trainer(self):
        print("i am being triggered")
        with self.client:
            response = self.client.post(
                url_for('index'), data = dict(
                    first_name = "May",
                    last_name = "Summer",
                    date_of_birth = "2000-04-03",
                    experience = 3,
                    certificates = "hello"
                )
            )
            self.assertIn(b'hi i am a trainer', response.data)
            
    


        