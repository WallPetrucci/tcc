from flask.views import MethodView

from api.User.Model.UserModel import UserModel


class UserController(MethodView):
    def get(self, id_cliente=None):
        user_model = UserModel()

        if isinstance(id_cliente, int) and id_cliente:
            result = user_model.get_user(id_cliente)
            return result
        else:
            pass
