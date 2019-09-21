from flask.views import MethodView
from flask import request
from backend.api.RecoverPassword.Schema import schemas
from voluptuous import MultipleInvalid, Invalid
from backend.api.RecoverPassword.Model.RecoverPasswordModel import RecoverPasswordModel


class RecoverPasswordController(MethodView):

    def post(self):
        try:
            user_data = request.get_json()
            schemas.schema_recovery(user_data)

            return RecoverPasswordModel.set_recovery_password(user_data.get('email'))

        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400
