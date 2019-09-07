from flask.views import MethodView
from flask import request

from backend.api.ResultsMetrics.Model.ResultsMetricsModel import ResultsMetricsModel
from backend.api.ResultsMetrics import constants as const


class ResultsMetricsController(MethodView):

    def get(self):
        return {'status': 'live'}

    def post(self):
        results_metrics = request.get_json()

        if all(item in results_metrics for item in const.LIST_KEYS_VALIDATIONS_RESULTS):
            model_results = ResultsMetricsModel(oximetry=results_metrics.get('ox'),
                                                heart=results_metrics.get('fc'),
                                                temperature=results_metrics.get('temp'),
                                                date_results=results_metrics.get('date'),
                                                User_idUser=results_metrics.get('User_idUser')
                                                )

            model_results.insert_results_metrics()
