from flask.views import MethodView


class RecoverPasswordController(MethodView):

    def get(self):
        return {'status': 'live'}
