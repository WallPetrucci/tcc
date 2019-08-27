from flask.views import MethodView
from flask import request

from backend.api.Monitor.Model.MonitorModel import MonitorModel


class MonitorController(MethodView):
    def get(self):
        return {'status': 'live'}

    def post(self):
        data_monitor = request.get_json()
        if data_monitor:
            salve = MonitorModel(data_monitor.get('name'), data_monitor.get('email'), data_monitor.get('telephone'))
            salve.insert_monitor()
