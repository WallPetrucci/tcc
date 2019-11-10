from flask.views import MethodView
from flask import request

from backend.api.ResultsMetrics.Model.ResultsMetricsModel import ResultsMetricsModel
# from backend.api.Devices.Model.DevicesModel import DevicesModel
# from backend.api.ResultsMetrics import constants as const
from voluptuous import MultipleInvalid, Invalid


class ResultsMetricsController(MethodView):

    def __init__(self):
        self.__results_model = ResultsMetricsModel()

    def get(self, id_user):

        try:

            results_metrics = ResultsMetricsModel.get_result_metrics(id_user)

            return results_metrics
        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400

    def post(self):
        try:
            metrics_data = request.get_json()

            return ResultsMetricsModel.has_alert(metrics_data)

        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400
