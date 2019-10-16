from flask.views import MethodView
from flask import request
from backend.api.Monitor.Model.MonitorModel import MonitorModel
from backend.api.Monitor.Schema import schemas
from voluptuous import MultipleInvalid, Invalid


class MonitorController(MethodView):
    def get(self):
        args_dict = request.args

        try:
            if not bool(args_dict):
                monitors = MonitorModel.query.all()
                json_monitors = list(map(lambda monitor: {'id': monitor.idMonitor,
                                                          'name': monitor.name,
                                                          'email': monitor.email,
                                                          'telephone': monitor.telephone}, monitors))
                return json_monitors
            else:
                monitor = MonitorModel.query.get(args_dict.get('id'))

            return {'id': monitor.idMonitor,
                    'name': monitor.name,
                    'email': monitor.email,
                    'telephone': monitor.telephone}
        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400

    def post(self):

        try:
            monitor_data = request.get_json()
            schemas.schema_insert_monitor(monitor_data)

            monitor_model = MonitorModel(name=monitor_data.get('name'),
                                         email=monitor_data.get('email'),
                                         telephone=monitor_data.get('telephone'))

            return monitor_model.insert_monitor(monitor_data.get('id_user'))
        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400

    def put(self, id_monitor):

        try:
            monitor_data = request.get_json()
            schemas.schema_update_monitor(monitor_data)

            return MonitorModel.update_monitor(id_monitor, monitor_data)
        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400

    def delete(self, id_monitor):

        try:
            return MonitorModel.delete_monitor(id_monitor)
        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400
