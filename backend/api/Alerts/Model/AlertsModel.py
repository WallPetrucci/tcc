from backend.api.model_base import AlertsBase, ResultsMetricsHasAlertsBase
from sqlalchemy import desc
from backend import db


class AlertsModel(AlertsBase):

    def __init__(self, **kwargs):
        super(AlertsModel, self).__init__(**kwargs)

    def insert_alert(self):
        db.session.add(self)
        db.session.commit()

        return {'msg': 'Alerta Inserido'}

    @staticmethod
    def get_alerts_from_user(user_id):
        alerts = []
        result = db.session.query(
            ResultsMetricsHasAlertsBase.ResultsMetrics_idResultsMetrics,
            ResultsMetricsHasAlertsBase.Alerts_idAlerts,
            AlertsModel.messages,
            AlertsModel.typeAlerts
        ).join(
            AlertsModel, AlertsModel.idAlerts == ResultsMetricsHasAlertsBase.Alerts_idAlerts
        ).filter(
            ResultsMetricsHasAlertsBase.ResultsMetrics_User_idUser == user_id
        ).order_by(desc(ResultsMetricsHasAlertsBase.ResultsMetrics_idResultsMetrics))

        for alert_list in result:
            alert = {
                'id_result_metrics': alert_list[0],
                'alert_id': alert_list[1],
                'alert_message': alert_list[2],
                'alert_type': alert_list[3]
            }
            alerts.append(alert)
        return alerts
