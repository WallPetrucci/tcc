from flask.views import MethodView


class AlertsController(MethodView):

    def get(self):
        return {'status': 'live'}
