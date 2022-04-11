from flask_testing import TestCase
from application import app, db
from application.models import Trainees, Trainers
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

class testViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)