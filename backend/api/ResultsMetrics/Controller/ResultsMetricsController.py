from flask.views import MethodView


class ResultsMetricsController(MethodView):

    def get(self):
        return {'status': 'live'}
