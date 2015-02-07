from HowMany import app, db
from HowMany.yo import Yo
from flask import jsonify, render_template, request

@app.route("/")
def index():
    count = Yo.query.count()
    return render_template("home.html", number=count)

@app.route("/callback")
def yo_callback():
    user = request.args['username']
    yo = Yo(sender=user)
    db.session.add(yo)
    db.session.commit()
    return jsonify(status="Success")