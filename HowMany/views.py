from HowMany import app, yo
from flask import jsonify, render_template, request

@app.route("/")
def index():
    return render_template("home.html", number=yo.total_yos)

@app.route("/callback")
def yo_callback():
    user = request.args['username']
    yo.add_yo(user)
    return jsonify(status="Success")