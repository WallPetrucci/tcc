from backend.api.model_base import UserBase
from backend import db


class UserModel(UserBase):

    def __init__(self, *args, **kwargs):
        super(UserModel, self).__init__(self, *args, **kwargs)
        self.base = UserBase()

    def insert_user(self):
        db.session.add(self.base)
        db.session.commit()
