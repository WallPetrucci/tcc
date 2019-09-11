from flask.views import MethodView
from flask import request

from backend.api.Address.Model.AddressModel import AddressModel
from backend.api.Address.Schema.schemas import schema_insert_address, schema_update_address
from voluptuous import MultipleInvalid, Invalid


class AddressController(MethodView):

    def get(self, id_user):
        try:
            address = AddressModel.query.filter_by(User_idUser=id_user).first()
            return{
                "street": address.street,
                "number": address.number,
                "city": address.city,
                "country": address.country,
                "state": address.state,
                "neighborhood": address.neighborhood,
                "User_idUser": address.User_idUser
            }
        except Exception as e:
            return {'msg': e}

    def post(self):

        try:
            address_data = request.get_json()

            schema_insert_address(address_data)

            address_model = AddressModel(street=address_data.get('street'),
                                         number=address_data.get('number'),
                                         city=address_data.get('city'),
                                         country=address_data.get('country'),
                                         state=address_data.get('state'),
                                         neighborhood=address_data.get('neighborhood'),
                                         User_idUser=address_data.get('User_idUser'),
                                         )

            return address_model.insert_address()
        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400

    def put(self, id_Address):

        try:
            address_data = request.get_json()

            schema_update_address(address_data)

            return AddressModel.update_address(id_Address, address_data)
        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400

    def delete(self, id_Address):

        try:
            return AddressModel.delete_address(id_Address)
        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400
