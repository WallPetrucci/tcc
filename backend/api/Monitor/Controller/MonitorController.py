from flask.views import MethodView
from flask import request
from flask import jsonify
from backend.api.model_base import MonitorBase


class MonitorController(MethodView):
    def get(self):
       	result =  MonitorBase.query.get(1)
        return jsonify({'developers':result.name})

    # def post(self):
    #     data_monitor = request.get_json()
    #     if data_monitor:
    #         salve = MonitorModel(data_monitor.get('name'), data_monitor.get('email'), data_monitor.get('telephone'))
    #         salve.insert_monitor()
