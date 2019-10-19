from backend.api.model_base import ResultsMetricsBase, ResultsMetricsHasAlertsBase
from backend.api.UserSettings.Model.UserSettingsModel import UserSettingsModel
from backend.api.Devices.Model.DevicesModel import DevicesModel
from backend.api.Alerts.Model.AlertsModel import AlertsModel
from backend import db
from datetime import datetime, timedelta
from backend.api.ResultsMetrics import constants as const


class ResultsMetricsModel(ResultsMetricsBase):
    heart_rate_average = 0
    oximetry_average = 0
    temperature_average = 0

    def __init__(self, **kwargs):
        super(ResultsMetricsModel, self).__init__(**kwargs)

    def insert_results_metrics(self, list_objects):
        # db.session.
        # db.session.commit()
        db.engine.execute(self.__table__.insert(), list_objects)

    @staticmethod
    def get_result_metrics(id_user):
        today_date = datetime.now()

        database_result_metrics = db.session.query(
            ResultsMetricsModel.date_results, db.func.avg(ResultsMetricsModel.oximetry),
            db.func.avg(ResultsMetricsModel.heart), db.func.avg(ResultsMetricsModel.temperature)
        ).filter(
            ResultsMetricsModel.date_results.between(today_date - timedelta(days=const.RESULT_METRICS_DAY), today_date)
        ).filter_by(User_idUser=id_user).group_by(db.func.cast(ResultsMetricsModel.date_results, db.Date)).all()

        result_metrics = {'oximetry': [], 'heart': [], 'temperature': []}

        for result in database_result_metrics:
            result_metrics.get('oximetry').append({'data': result[0].strftime("%d-%m-%Y"), 'result': result[1]})
            result_metrics.get('heart').append({'data': result[0].strftime("%d-%m-%Y"), 'result': result[2]})
            result_metrics.get('temperature').append({'data': result[0].strftime("%d-%m-%Y"), 'result': result[3]})

        return result_metrics

    @classmethod
    def has_alert(cls, metrics_list):
        for metric in metrics_list:
            cls.heart_rate_average += metric.get('heart')
            cls.oximetry_average += metric.get('oximetry')
            cls.temperature_average += metric.get('temperature')

        cls.heart_rate_average /= len(metrics_list)
        cls.oximetry_average /= len(metrics_list)
        cls.temperature_average /= len(metrics_list)

        user_settings = cls.__get_user_settings(metrics_list[0].get('whm_id'))

        alert_list = cls.__check_metric_has_exceeded(user_settings)

        if not alert_list:
            return {'msg': 'Não há alertas', 'alerts': alert_list}

        for alert in alert_list:
            alerts_model = AlertsModel(messages=alert.get('message'), typeAlerts=alert.get('alert_type'))
            alerts_model.insert_alert()

        return {'msg': 'Verifique seus alertas', 'alerts': alert_list}

    @classmethod
    def __get_user_settings(cls, whm_id):
        settings = DevicesModel.query.add_columns(
            UserSettingsModel.User_idUser.label('user_id'),
            UserSettingsModel.heartRate.label('heart_rate'),
            UserSettingsModel.heartRate.label('oximetry'),
            UserSettingsModel.heartRate.label('temperature'),
            UserSettingsModel.heartRate.label('active_alert_heart_rate'),
            UserSettingsModel.heartRate.label('active_alert_oximetry'),
            UserSettingsModel.heartRate.label('active_alert_temperature'),
        ).join(
            UserSettingsModel, UserSettingsModel.User_idUser == DevicesModel.User_idUser
        ).filter(DevicesModel.idHardware == whm_id).first()

        user_settings = {
            'user_id': settings.user_id,
            'heart_rate': settings.heart_rate,
            'oximetry': settings.oximetry,
            'temperature': settings.temperature,
            'active_alert_heart_rate': True if settings.active_alert_heart_rate else False,
            'active_alert_oximetry': True if settings.active_alert_oximetry else False,
            'active_alert_temperature': True if settings.active_alert_temperature else False,
        }

        return user_settings

    @classmethod
    def __check_metric_has_exceeded(cls, user_settings):
        alerts = []

        if user_settings.get('active_alert_heart_rate'):
            if cls.heart_rate_average > float(user_settings.get('heart_rate').get('max')):
                alerts.append({
                    'alert_type': 'Frequência Cardíaca',
                    'message': 'Frequência Cardíaca Alta',
                    'heart_rate': cls.heart_rate_average,
                    'oximetry': cls.oximetry_average,
                    'temperature': cls.temperature_average,
                })
            elif cls.heart_rate_average < float(user_settings.get('heart_rate').get('min')):
                alerts.append({
                    'alert_type': 'Frequência Cardíaca',
                    'message': 'Frequência Cardíaca Baixa',
                    'heart_rate': cls.heart_rate_average,
                    'oximetry': cls.oximetry_average,
                    'temperature': cls.temperature_average,
                })

        if user_settings.get('active_alert_oximetry'):
            if cls.oximetry_average > float(user_settings.get('oximetry').get('max')):
                alerts.append({
                    'alert_type': 'Oximetria',
                    'message': 'Oximetria Alta',
                    'heart_rate': cls.heart_rate_average,
                    'oximetry': cls.oximetry_average,
                    'temperature': cls.temperature_average,
                })
            elif cls.oximetry_average < float(user_settings.get('oximetry').get('min')):
                alerts.append({
                    'alert_type': 'Oximetria',
                    'message': 'Oximetria Baixa',
                    'heart_rate': cls.heart_rate_average,
                    'oximetry': cls.oximetry_average,
                    'temperature': cls.temperature_average,
                })

        if user_settings.get('active_alert_temperature'):
            if cls.temperature_average > float(user_settings.get('temperature').get('max')):
                alerts.append({
                    'alert_type': 'Temperatura',
                    'message': 'Temperatura Alta',
                    'heart_rate': cls.heart_rate_average,
                    'oximetry': cls.oximetry_average,
                    'temperature': cls.temperature_average,
                })
            elif cls.temperature_average < float(user_settings.get('temperature').get('min')):
                alerts.append({
                    'alert_type': 'Temperatura Baixa',
                    'alert_type': 'Temperatura Baixa',
                    'heart_rate': cls.heart_rate_average,
                    'oximetry': cls.oximetry_average,
                    'temperature': cls.temperature_average,
                })

        return alerts
