# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Date(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable=False)
    date_id = db.Column(db.Integer, db.ForeignKey('date.id'), nullable=False)
    date = db.relationship('Date', backref=db.backref('bookings', lazy=True))
    activity = db.relationship('Activity', backref=db.backref('bookings', lazy=True))
    __table_args__ = (db.UniqueConstraint('activity_id', 'date_id', name='_activity_date_uc'),)

