from backend import db


class Alerts(db.Model):

    __table__ = 'Alerts'
    idAlerts = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.String(100), unique=False, nullable=True)
    typeAlerts = db.Column(db.String(45), unique=False, nullable=True)

    def __init__(self, messages, type_alerts):
        self.messages = messages
        self.type_alerts = type_alerts
