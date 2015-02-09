import os
import redis
from flask import Flask
from flask.ext.heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy
from flask_sockets import Sockets
from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['REDIS_URL'] = os.environ['REDISCLOUD_URL']
app.config['REDIS_CHAN'] = "howmany"

db=SQLAlchemy(app)
heroku = Heroku(app)
sentry = Sentry(app)
redis = redis.from_url(app.config['REDIS_URL'])
sockets = Sockets(app)

from HowMany.ws import Backend
backend = Backend()

key = os.environ['APP_KEY']

from HowMany import views, filters, yo