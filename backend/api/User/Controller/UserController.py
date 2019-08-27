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
        data_client = request.get_json()

        if data_client:
            user_model = UserModel(data_client)
            user_model.insert_user()
            return user_model

        return "Passa a porra do JSON!"
