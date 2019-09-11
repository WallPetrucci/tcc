from backend.api.model_base import AddressBase
from backend import db


class AddressModel(AddressBase):

    def __init__(self, **kwargs):
        super(AddressModel, self).__init__(**kwargs)

    def insert_address(self):
        db.session.add(self)
        db.session.commit()

        return {'id_Address': self.idAddress}

    @staticmethod
    def update_address(id_Address, address_data):
        AddressModel.query.filter_by(idAddress=id_Address).update(address_data)
        db.session.commit()

        return {'id_Address': id_Address, 'msg': 'Endereço atualizado com sucesso'}

    @staticmethod
    def delete_address(id_Address):
        db.session.delete(AddressModel.query.filter_by(idAddress=id_Address).first())
        db.session.commit()
        return {'msg': 'Endereço excluído com sucesso'}
