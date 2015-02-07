from flask import Flask
from flask.ext.heroku import Heroku
from raven.contrib.flask import Sentry

from HowMany.yo import Yo

app = Flask(__name__)
heroku = Heroku(app)
sentry = Sentry(app)

yo = Yo()

from HowMany import views