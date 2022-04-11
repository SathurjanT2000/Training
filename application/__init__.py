from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from Secrets import SQLALCHEMY_DATABASE_URI
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = str(uuid.uuid4)

db = SQLAlchemy(app)

from application import routes
