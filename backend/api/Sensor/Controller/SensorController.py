from flask.views import MethodView


class SensorController(MethodView):

    def get(self):
        return {'status': 'live'}
