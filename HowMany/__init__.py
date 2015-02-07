from flask import Flask
from flask.ext.heroku import Heroku

from HowMany.yo import Yo

app = Flask(__name__)
heroku = Heroku(app)
yo = Yo()


from HowMany import views