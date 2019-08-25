from flask.views import MethodView


class DevicesController(MethodView):

    def get(self):
        return {'status': 'live'}
