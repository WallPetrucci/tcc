from flask.views import MethodView
from flask import request

from backend.api.Login.Model.LoginModel import LoginModel
from backend.api.Login.Schema import schemas
from voluptuous import MultipleInvalid, Invalid


class LoginController(MethodView):

    def post(self):
        try:
            login_data = request.get_json()
            schemas.schema_login(login_data)

            return LoginModel.do_login(user_email=login_data.get('email'), user_password=login_data.get('password'))

        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400

    def delete(self):
        try:
            user_data = request.get_json()

            schemas.schema_logout(user_data)

            return LoginModel.do_logout(user_email=user_data.get('email'), user_name=user_data.get('name'))

        except MultipleInvalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Invalid as e:
            return {'sucesso': False, 'msg': str(e)}, 400

        except Exception as e:
            return {'sucesso': False, 'msg': str(e)}, 400
