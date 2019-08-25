from flask.views import MethodView


class UserSettingsController(MethodView):

    def get(self):
        return {'status': 'live'}
