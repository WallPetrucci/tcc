from flask.views import MethodView
from backend.api.Monitor.MonitorModel import MonitorModel


class MonitorController(MethodView):
    def get(self):
        return MonitorModel.query.all()

    # def post(self):
    #     data_monitor = request.get_json()
    #     if data_monitor:
    #         salve = MonitorModel(data_monitor.get('name'), data_monitor.get('email'), data_monitor.get('telephone'))
    #         salve.insert_monitor()
