from flask.views import MethodView
from flask import request
from backend.api.Monitor.Model.MonitorModel import MonitorModel


class MonitorController(MethodView):
    def get(self):
        json_monitors = []
        args_dict = request.args

        try:
            if not bool(args_dict):
                monitor_model = MonitorModel.query.all()
                for monitor in monitor_model:
                    json_monitors.append({
                        'name': monitor.name,
                        'email': monitor.email,
                        'telephone': monitor.telephone
                    })

                return json_monitors
            else:
                monitor_model = MonitorModel.query.get(args_dict.get('id'))

            return {
                'name': monitor_model.name,
                'email': monitor_model.email,
                'telephone': monitor_model.telephone
            }
        except Exception as e:
            return {e}

    def post(self):
        data_monitor = request.get_json()
        if data_monitor:
            monitor_model = MonitorModel(data_monitor.get('name'), data_monitor.get('email'), data_monitor.get('telephone'))
            monitor_model.insert_monitor()
