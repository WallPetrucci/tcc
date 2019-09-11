from backend.api.model_base import UserSettingsBase
from backend import db


class UserSettingsModel(UserSettingsBase):

    def __init__(self, **kwargs):
        super(UserSettingsModel, self).__init__(**kwargs)

    def insert_settings(self):
        db.session.add(self)
        db.session.commit()

        return {'id_settings': self.idUserSettings}

    @staticmethod
    def update_settings(id_Settings, user_settings_data):
        UserSettingsModel.query.filter_by(idUserSettings=id_Settings).update(user_settings_data)
        db.session.commit()

        return {'id_Settings': id_Settings, 'msg': 'Configurações atualizadas com sucesso'}
