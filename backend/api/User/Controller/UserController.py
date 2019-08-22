from flask.views import MethodView


class UserController(MethodView):
    def get(self, id_cliente):
        return {
            'sucesso': False,
            'id_cliente': id_cliente
        }
