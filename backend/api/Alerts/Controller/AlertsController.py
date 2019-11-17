from flask.views import MethodView
from voluptuous import MultipleInvalid, Invalid
from backend.api.Alerts.Model.AlertsModel import AlertsModel


class AlertsController(MethodView):

    def get(self, user_id):
        try:

            return AlertsModel.get_alerts_from_user(user_id)
        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}
