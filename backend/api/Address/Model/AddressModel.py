from backend.api.model_base import AddressBase
from backend import db


class AddressModel(AddressBase):

    def __init__(self, **kwargs):
        super(AddressModel, self).__init__(**kwargs)

    def insert_address(self):
        db.session.add(self)
        db.session.commit()

        return {'id_Address': self.idAddress}
