from HowMany import db


class Yo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String)
    sent_at = db.Column(db.DateTime)