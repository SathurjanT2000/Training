from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = #To be assigned later
app.config['SECRET_KEY'] = #To be assigned later

db = SQLAlchemy(app)

from application import routes
