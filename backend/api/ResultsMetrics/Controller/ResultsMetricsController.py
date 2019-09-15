from flask.views import MethodView
from flask import request

from backend.api.ResultsMetrics.Model.ResultsMetricsModel import ResultsMetricsModel
# from backend.api.Devices.Model.DevicesModel import DevicesModel
# from backend.api.ResultsMetrics import constants as const


class ResultsMetricsController(MethodView):

    def get(self, id_user):

        try:

            results_metrics = ResultsMetricsModel.get_result_metrics(id_user)

            return results_metrics
        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400

    def post(self):
        results_metrics = request.get_json()
        results_model = ResultsMetricsModel()

        print(results_metrics)

        results_model.insert_results_metrics(results_metrics)
