import os
from flask import Flask
from flask.ext.heroku import Heroku
from flask_redis import Redis
from flask.ext.sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['REDIS_URL'] = os.environ['REDISCLOUD_URL']

db=SQLAlchemy(app)
heroku = Heroku(app)
sentry = Sentry(app)
redis_store = Redis(app)

key = os.environ['APP_KEY']

from HowMany import views, filters, yo