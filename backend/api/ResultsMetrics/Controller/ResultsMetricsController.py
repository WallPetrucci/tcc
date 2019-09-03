from flask.views import MethodView
from flask import request

from backend.api.Monitor.Model.ResultsMetricsModel import ResultsMetricsModel
from constants import constants as const


class ResultsMetricsController(MethodView):

    def get(self):
        return {'status': 'live'}

    def post(self):
        results_metrics = request.get_json()

        if all(item in results_metrics for item in const.LIST_KEYS_VALIDATIONS_RESULTS):
            ResultsMetricsModel(oximetry=results_metrics.get('ox'),
                                heart=results_metrics.get('fc'),
                                temperature=results_metrics.get('temp'),
                                date_results=results_metrics.get('date'),
                                whm=results_metrics.get('whm')
                                )

            return ResultsMetricsModel.insert_results_metrics()
