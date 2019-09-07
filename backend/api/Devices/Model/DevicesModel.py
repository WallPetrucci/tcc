from backend.api.model_base import DevicesBase
from backend import db


class DevicesModel(DevicesBase):

    def __init__(self, **kwargs):
        super(DevicesModel, self).__init__(**kwargs)

    def insert_device(self):
        db.session.add(self)
        db.session.commit()

        return {'id_device': self.idDevices}
