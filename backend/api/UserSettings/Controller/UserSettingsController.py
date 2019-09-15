from flask.views import MethodView
from flask import request

from backend.api.UserSettings.Model.UserSettingsModel import UserSettingsModel
from voluptuous import MultipleInvalid, Invalid
from backend.api.UserSettings.Schema import schemas


class UserSettingsController(MethodView):

    def get(self, id_User):
        try:
            settings = UserSettingsModel.query.filter_by(User_idUser=id_User).first()

            return {
                'id_Settings': settings.idUserSettings,
                'heartRate': settings.heartRate,
                'oximetry': settings.oximetry,
                'temperature': settings.temperature,
                'activeAlertOximetry': settings.activeAlertOximetry,
                'activeAlertHeartRate': settings.activeAlertHeartRate,
                'activeAlertTemperature': settings.activeAlertTemperature,
                'User_idUser': settings.User_idUser
            }
        except Exception as e:
            return {'msg': e}

    def post(self):
        try:
            user_settings_data = request.get_json()

            schemas.schema_insert_settings(user_settings_data)

            user_settings_model = UserSettingsModel(
                heartRate=user_settings_data.get('heartRate'),
                oximetry=user_settings_data.get('oximetry'),
                temperature=user_settings_data.get('temperature'),
                activeAlertOximetry=user_settings_data.get('activeAlertOximetry'),
                activeAlertHeartRate=user_settings_data.get('activeAlertHeartRate'),
                activeAlertTemperature=user_settings_data.get('activeAlertTemperature'),
                User_idUser=user_settings_data.get('User_idUser'),
            )

            return user_settings_model.insert_settings()

        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400

    def put(self, id_Settings):
        try:
            user_settings_data = request.get_json()

            schemas.schema_update_settings(user_settings_data)

            return UserSettingsModel.update_settings(id_Settings, user_settings_data)

        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400
