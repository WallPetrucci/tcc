from backend.api.model_base import UserSettingsBase
from backend import db


class UserSettingsModel(UserSettingsBase):

    def __init__(self, **kwargs):
        super(UserSettingsModel, self).__init__(**kwargs)

    def insert_settings(self):
        db.session.add(self)
        db.session.commit()

        return {'id_settings': self.idUserSettings}
