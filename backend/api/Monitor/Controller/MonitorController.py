from flask.views import MethodView
from flask import request
from backend.api.Monitor.Model.MonitorModel import MonitorModel
from backend.api.model_base import UserHasMonitorBase
from backend.api.Monitor.Schema import schemas
from voluptuous import MultipleInvalid, Invalid


class MonitorController(MethodView):
    def get(self, id):
        try:

            monitor_list = MonitorModel.query.join(
                UserHasMonitorBase, UserHasMonitorBase.Monitor_idMonitor == MonitorModel.idMonitor
            ).filter(UserHasMonitorBase.User_idUser == id).all()

            monitors_info = list(map(lambda monitor: {'id': monitor.idMonitor,
                                                      'name': monitor.name,
                                                      'email': monitor.email,
                                                      'telephone': monitor.telephone}, monitor_list))
            return monitors_info

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

    def put(self, id):

        try:
            monitor_data = request.get_json()
            schemas.schema_update_monitor(monitor_data)

            return MonitorModel.update_monitor(id, monitor_data)
        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400

    def delete(self, id):

        try:
            return MonitorModel.delete_monitor(id)
        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400
