import datetime
from HowMany import db


def get_current_time():
    return datetime.datetime.utcnow()


class Yo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String)
    sent_at = db.Column(db.DateTime, default=get_current_time)