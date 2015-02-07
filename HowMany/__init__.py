from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

total_yos = 0
yos = {}