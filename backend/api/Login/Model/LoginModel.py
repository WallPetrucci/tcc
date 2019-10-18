from backend.api.User.Model.UserModel import UserModel
from flask import session


class LoginModel:

    @staticmethod
    def do_login(user_email, user_password):
        user = UserModel.get_user_by_login(user_email=user_email, user_password=user_password, logged_in=1)

        if user:
            return user

        return {'msg': "Não foi possível efetuar o login"}, 400

    @staticmethod
    def do_logout(user_email, user_name):
        user = UserModel.do_logout(user_email=user_email, user_name=user_name, logged_in=0)
        if user:
            return {'msg': "Logout efetuado com sucesso"}, 200

        return {'msg': "Não foi possível efetuar o logout"}, 200
