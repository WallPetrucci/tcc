from backend.api.model_base import MonitorBase
from backend import db


class MonitorModel(MonitorBase):

    def __init__(self, name, email, cel):
        self.base = MonitorBase(name, email, cel)

    def insert_monitor(self):
        db.session.add(self.base)
        db.session.commit()
