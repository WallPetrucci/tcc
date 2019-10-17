from flask.views import MethodView
from flask import request

from backend.api.User.Model.UserModel import UserModel
from voluptuous import MultipleInvalid, Invalid
from backend.api.User.Schema import schemas


class UserController(MethodView):
    def get(self, id_cliente=None):
        user_model = UserModel()

        if isinstance(id_cliente, int) and id_cliente:
            result = user_model.get_user(id_cliente)
            return result
        else:
            pass

    def post(self):
        try:
            user_data = request.get_json()
            schemas.schema_insert_user(user_data)
            user_model = UserModel(name=user_data.get('nomeRegistro'), dateBirth=user_data.get('niverRegistro'),
                                   email=user_data.get('emailRegistro'), password=user_data.get('senhaRegistro'),
                                   cel=user_data.get('celRegistro'), is_loggedin=0)

            return user_model.insert_user()

        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400
