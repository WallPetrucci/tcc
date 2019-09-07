from flask.views import MethodView
from flask import request
from backend.api.Devices.Model.DevicesModel import DevicesModel


class DevicesController(MethodView):

    def get(self):
        return {'status': 'live'}

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
