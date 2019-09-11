from flask.views import MethodView
from flask import request

from backend.api.Address.Model.AddressModel import AddressModel
from backend.api.Address.Schema.schemas import schema_insert_address
from voluptuous import MultipleInvalid, Invalid


class AddressController(MethodView):

    def get(self, id_User):
        pass
        try:
            settings = AddressModel.query.filter_by(User_idUser=id_User).first()

            return {
                'id_Settings': settings.idAddress,
                'heartRate': settings.heartRate,
                'oximetry': settings.oximetry,
                'temperature': settings.temperature,
                'acitveAlertOximetry': settings.acitveAlertOximetry,
                'activeAlertHeartRate': settings.activeAlertHeartRate,
                'activeAlertBTemperature': settings.activeAlertBTemperature,
                'User_idUser': settings.User_idUser
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
