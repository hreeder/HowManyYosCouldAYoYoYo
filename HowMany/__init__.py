from flask import Flask
from flask.ext.heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)
app.config.from_object('config')

total_yos = 0
yos = {}