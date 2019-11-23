from backend.api.model_base import UserBase
from backend import db


class UserModel(UserBase):

    def __init__(self, **kwargs):
        super(UserModel, self).__init__(**kwargs)

    def insert_user(self):
        db.session.add(self)
        db.session.commit()

        return {'id_user': self.idUser}

    @staticmethod
    def get_user_by_login(user_email, user_password, logged_in):
        user = UserModel.query.filter_by(email=user_email, password=user_password).first()

        user.is_loggedin = logged_in
        db.session.commit()

        if user:
            return {'id': user.idUser, 'email': user.email, 'name': user.name, 'logged_in': user.is_loggedin}

        return {'sucesso': False, "msg": "Usuário não encontrado"}

    @staticmethod
    def do_logout(user_email, user_name, logged_in):
        user = UserModel.query.filter_by(email=user_email, name=user_name).first()

        user.is_loggedin = logged_in
        db.session.commit()

        if user:
            return {'id': user.idUser, 'email': user.email, 'name': user.name, 'logged_in': user.is_loggedin}

        return {'sucesso': False, "msg": "Usuário não encontrado"}

    @staticmethod
    def update_user(id, user_data):
        try:
            UserModel.query.filter_by(idUser=id).update(user_data)
            db.session.commit()
            return {'idUser': id, 'msg': 'Informações atualizadas com sucesso !'}
        except Exception as e:
            return {'msg': str(e)}
