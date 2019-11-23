import random

from datetime import datetime
from backend.api.model_base import RecoverPasswordBase
from backend.api.User.Model.UserModel import UserModel
from backend import db
from backend.api.utils.EmailSender import Sender
from backend.api.utils import constants as const_email


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
            email_sender = Sender()
            email_sender.set_header([user_email], const_email.EMAIL_DEST, const_email.SUBJECT)
            email_sender.set_msg(const_email.RECOVERY.format(user.password), 'html')
            email_sender.send_message()
            return {
                'msg': 'Enviamos as instruções para recuperação de senha em seu email',
            }
        return {'msg': 'Não Encontramos seu email em nossa base', 'sucesso': False}
