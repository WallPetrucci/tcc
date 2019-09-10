from flask.views import MethodView
from flask import request

from backend.api.UserSettings.Model.UserSettingsModel import UserSettingsModel


class UserSettingsController(MethodView):

    def get(self, id_User):
        try:
            settings = UserSettingsModel.query.filter_by(User_idUser=id_User).first()

            return {
                'id_Settings': settings.idUserSettings,
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
        user_settings_data = request.get_json()

        if user_settings_data:
            user_settings_model = UserSettingsModel(heartRate=user_settings_data.get('heartRate'),
                                                    oximetry=user_settings_data.get('oximetry'),
                                                    temperature=user_settings_data.get('temperature'),
                                                    acitveAlertOximetry=user_settings_data.get('acitveAlertOximetry'),
                                                    activeAlertHeartRate=user_settings_data.get('activeAlertHeartRate'),
                                                    activeAlertBTemperature=user_settings_data.get(
                                                        'activeAlertBTemperature'),
                                                    User_idUser=user_settings_data.get('User_idUser'),
                                                    )

            return user_settings_model.insert_settings()

        return {'sucesso': False}, 400
