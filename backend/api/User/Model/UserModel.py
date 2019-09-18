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
    def get_user_by_login(user_email, user_password):
        user = db.session.query(
            UserModel.idUser,
            UserModel.email,
            UserModel.name
        ).filter_by(email=user_email, password=user_password).first()

        if user:
            return {'id': user.idUser, 'email': user.email, 'name ': user.name}

        return {'sucesso': False, "msg": "Usuário não encontrado"}
