from backend.api.model_base import AlertsBase, ResultsMetricsHasAlertsBase, ResultsMetricsBase
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
            ResultsMetricsBase.date_results,
            ResultsMetricsBase.heart,
            ResultsMetricsBase.oximetry,
            ResultsMetricsBase.temperature,
            AlertsModel.messages,
            AlertsModel.typeAlerts
        ).join(
            AlertsModel, AlertsModel.idAlerts == ResultsMetricsHasAlertsBase.Alerts_idAlerts
        ).join(
            ResultsMetricsBase,
            ResultsMetricsBase.idResultsMetrics == ResultsMetricsHasAlertsBase.ResultsMetrics_idResultsMetrics
        ).filter(
            ResultsMetricsHasAlertsBase.ResultsMetrics_User_idUser == user_id
        ).order_by(desc(ResultsMetricsBase.date_results), desc(ResultsMetricsHasAlertsBase.Alerts_idAlerts)).limit(5)

        for alert_list in result:
            alert = {
                'id_result_metrics': alert_list[0],
                'alert_id': alert_list[1],
                'alert_date': alert_list[2].isoformat(),
                'heart': alert_list[3],
                'oximetry': alert_list[4],
                'temperature': alert_list[5],
                'messages': alert_list[6],
                'alert_type': alert_list[7]
            }
            alerts.append(alert)
        return alerts
