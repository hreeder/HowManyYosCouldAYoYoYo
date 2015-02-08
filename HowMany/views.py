from HowMany import app, db, key
from HowMany.yo import Yo
from flask import jsonify, render_template, request, make_response
from sqlalchemy import desc


@app.route("/")
def index():
    count = Yo.query.count()
    latest = Yo.query.order_by(desc(Yo.sent_at)).limit(5).all()
    most = db.session.query(Yo.sender, db.func.count(Yo.sender).label("count")).group_by(Yo.sender).order_by(
        "count DESC").limit(5).all()
    return render_template("home.html", number=count, latest=latest, most=most)


@app.route("/callback/<token>")
def yo_callback(token):
    if token == key:
        user = request.args['username']
        yo = Yo(sender=user)
        db.session.add(yo)
        db.session.commit()
        return jsonify(status="Success")
    else:
        return make_response(jsonify(status="Token Invalid"), 403)