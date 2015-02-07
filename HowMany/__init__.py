import os
from flask import Flask
from flask.ext.heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db=SQLAlchemy(app)
heroku = Heroku(app)
sentry = Sentry(app)

from HowMany import views