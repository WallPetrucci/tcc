from flask.views import MethodView
from flask import request

from backend.api.User.Model.UserModel import UserModel


class UserController(MethodView):
    def get(self, id_cliente=None):
        user_model = UserModel()

        if isinstance(id_cliente, int) and id_cliente:
            result = user_model.get_user(id_cliente)
            return result
        else:
            pass

    def post(self):
        user_data = request.get_json()

        if user_data:
            user_model = UserModel(name=user_data.get('nomeRegistro'),
                                   dateBirth=user_data.get('niverRegistro'),
                                   email=user_data.get('emailRegistro'),
                                   password=user_data.get('senhaRegistro'),
                                   cel=user_data.get('celRegistro'),
                                   )
            user_model.insert_user()
            return user_model.insert_user()

        return {'sucesso': False}, 400
