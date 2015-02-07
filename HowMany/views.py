from HowMany import app, total_yos, yos
from flask import jsonify, render_template, request

@app.route("/")
def index():
    return render_template("home.html", number=total_yos)

@app.route("/callback")
def yo_callback():
    total_yos += 1
    user = request.args.get('username')
    if user in yos.keys():
        yos[user] += 1
    else:
        yos[user] = 1
    return jsonify(status="OK")