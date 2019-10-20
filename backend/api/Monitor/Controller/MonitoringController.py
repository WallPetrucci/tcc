from flask.views import MethodView
from flask import request
from backend.api.Monitor.Model.MonitorModel import MonitorModel
from backend.api.Monitor.Schema import schemas
from voluptuous import MultipleInvalid, Invalid


class MonitoringController(MethodView):

    def post(self):

        try:
            token = request.get_json()
            schemas.schema_monitoring(token)

            return MonitorModel.monitoring(token.get('token'))
        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400
