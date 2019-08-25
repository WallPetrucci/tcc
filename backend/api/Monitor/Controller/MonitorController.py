from flask.views import MethodView


class MonitorController(MethodView):

    def get(self):
        return {'status': 'live'}
