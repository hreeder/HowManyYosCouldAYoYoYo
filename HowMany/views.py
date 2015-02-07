from HowMany import app, db
from HowMany.yo import Yo
from flask import jsonify, render_template, request
from sqlalchemy import desc


@app.route("/")
def index():
    count = Yo.query.count()
    latest = Yo.query.order_by(desc(Yo.sent_at)).limit(5).all()
    most = db.session.query(Yo.sender, db.func.count(Yo.sender).label("count")).group_by(Yo.sender).order_by(
        "count DESC").limit(5).all()
    return render_template("home.html", number=count, latest=latest, most=most)


@app.route("/callback")
def yo_callback():
    user = request.args['username']
    yo = Yo(sender=user)
    db.session.add(yo)
    db.session.commit()
    return jsonify(status="Success")