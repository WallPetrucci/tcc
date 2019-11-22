from flask.views import MethodView
from flask import request
from backend.api.Devices.Model.DevicesModel import DevicesModel


class DevicesController(MethodView):

    def get(self, user_id):
        try:
            device = DevicesModel.query.filter_by(User_idUser=user_id).first()
            if device:
                return {
                    'whm_id': device.idHardware
                }

            return {'msg': 'Não foram encontrados devices para o usuario informado'}
        except Exception as e:
            return {'msg': e}

    def post(self):
        device_data = request.get_json()

        try:
            if device_data:
                device_model = DevicesModel(idHardware=device_data.get('idHardware'),
                                            User_idUser=device_data.get('User_idUser'))

                return device_model.insert_device()
            return {'sucesso': False}
        except Exception as e:
            return {'msg': e}
