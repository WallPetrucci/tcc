from backend.api.User.Model.UserModel import UserModel
from flask import session


class LoginModel:

    @staticmethod
    def do_login(user_email, user_password):
        user = UserModel.get_user_by_login(user_email=user_email, user_password=user_password)

        if user:
            session.update({'logged_in': True, 'user': user.get('name'), 'email': user.get('name')})
            return user

        return {'msg': "Não foi possível efetuar o login"}, 400
