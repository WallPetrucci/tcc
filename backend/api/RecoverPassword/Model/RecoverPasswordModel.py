import random

from datetime import datetime
from backend.api.model_base import RecoverPasswordBase
from backend.api.User.Model.UserModel import UserModel
from backend import db


class RecoverPasswordModel(RecoverPasswordBase):

    def __init__(self, **kwargs):
        super(RecoverPasswordModel, self).__init__(**kwargs)

    @staticmethod
    def set_recovery_password(user_email):
        user = UserModel.query.filter_by(email=user_email).first()
        # TODO Send email

        if user:
            code_confirm = random.getrandbits(128)
            now = datetime.now()

            recovery_to_insert = RecoverPasswordModel(dateTime=now, codeConfirm=code_confirm, expiration=0,
                                                      User_idUser=user.idUser)
            db.session.add(recovery_to_insert)
            db.session.commit()

            return {
                'msg': 'Enviamos as instruções para recuperação de senha em seu email',
            }
        return {'msg': 'Não Encontramos seu email em nossa base', 'sucesso': False}
