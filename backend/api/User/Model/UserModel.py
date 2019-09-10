from backend.api.model_base import UserBase
from backend import db


class UserModel(UserBase):

    def __init__(self, **kwargs):
        super(UserModel, self).__init__(**kwargs)

    def insert_user(self):
        db.session.add(self)
        db.session.commit()

        return {'id_user': self.idUser}
