from backend.api.model_base import MonitorBase
from backend import db


class MonitorModel(MonitorBase):

    def __init__(self, **kwargs):
        super(MonitorModel, self).__init__(**kwargs)

    def insert_monitor(self):
        db.session.add(self)
        db.session.commit()

        return {'id_monitor': self.idMonitor}
