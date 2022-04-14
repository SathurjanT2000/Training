from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
#The following method is used because on the vm, i am using a secret file to import my database URI and on jenkins, i am using credential.
try:
    from Secrets import SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
except:
    from os import getenv
    app.config['SQLALCHEMY_DATABASE_URI'] = "SQLALCHEMY_DATABASE_URI"

app.config['SECRET_KEY'] = str(uuid.uuid4)

db = SQLAlchemy(app)

from application import routes
