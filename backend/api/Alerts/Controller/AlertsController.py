from backend.api.Alerts.Model.AlertsModel import Alerts
from flask import MethodView


class AlertsController(MethodView):

    def get(self):

        meus_alertas = Alerts.query.all()

        return meus_alertas
