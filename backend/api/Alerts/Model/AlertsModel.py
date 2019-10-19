from backend.api.model_base import AlertsBase
from backend import db


class AlertsModel(AlertsBase):

    def __init__(self, **kwargs):
        super(AlertsModel, self).__init__(**kwargs)

    def insert_alert(self):
        db.session.add(self)
        db.session.commit()

        return {'msg': 'Alerta Inserido'}
