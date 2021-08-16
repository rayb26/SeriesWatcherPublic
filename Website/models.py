# Code created by Rayhan Biju 2021
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Following code was never sent to production since we never deployed our login service. 
class Alert(db.Model):
    title_id = db.Column(db.String(150), primary_key=True)
    title = db.Column(db.String(2000))
    episodes = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    alerts = db.relationship('Alert')
