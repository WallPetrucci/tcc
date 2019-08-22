from flask.views import MethodView


class HealthCheck(MethodView):

    def get(self):
        return {'status': 'live'}
