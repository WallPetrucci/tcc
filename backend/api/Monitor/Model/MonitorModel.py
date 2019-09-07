from backend.api.model_base import MonitorBase
from backend import db


class MonitorModel(MonitorBase):

    def __init__(self, name, email, telephone):
        self.base = MonitorBase()

    def insert_monitor(self):
        db.session.add(self.base)
        db.session.commit()
