from backend.api.User.Model.UserModel import UserModel
from flask import session


class LoginModel:

    @staticmethod
    def do_login(user_email, user_password):
        user = UserModel.get_user_by_login(user_email=user_email, user_password=user_password)

        if user:
            session.update({'logged_in': True, 'user': user.get('name'), 'email': user.get('email')})
            return user

        return {'msg': "Não foi possível efetuar o login"}, 400

    @staticmethod
    def do_logout(user_email, user_name):

        if user_email in session and user_name in session:
            session.pop('logged_in', None)
            session.pop('user', None)
            session.pop('email', None)

            return {'msg': "Logout efetuado com sucesso"}, 200

        return {'msg': "Não foi possível efetuar o logout"}, 200
