from flask.views import MethodView
from flask import request

from backend.api.User.Model.UserModel import UserModel
from backend.api.Login.Schema import schemas
from voluptuous import MultipleInvalid, Invalid


class LoginController(MethodView):

    def post(self):
        try:
            login_data = request.get_json()
            schemas.schema_login(login_data)

            return UserModel.get_user_by_login(user_email=login_data.get('email'),
                                               user_password=login_data.get('password'))

        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400
