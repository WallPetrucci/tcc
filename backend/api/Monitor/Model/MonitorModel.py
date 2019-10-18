from backend.api.model_base import MonitorBase, UserHasMonitorBase
from backend import db
import random
import string


class MonitorModel(MonitorBase):

    def __init__(self, **kwargs):
        super(MonitorModel, self).__init__(**kwargs)

    def insert_monitor(self, id_user):
        db.session.add(self)
        db.session.commit()

        hash_monitor = "{}{}{}".format(id_user, ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
                                       self.idMonitor)

        user_has_monitor = UserHasMonitorBase(User_idUser=id_user, Monitor_idMonitor=self.idMonitor, token=hash_monitor)
        db.session.add(user_has_monitor)
        db.session.commit()

        return {'id_monitor': self.idMonitor, 'token': hash_monitor}

    @staticmethod
    def update_monitor(id_monitor, monitor_data):
        MonitorModel.query.filter_by(idMonitor=id_monitor).update(monitor_data)
        db.session.commit()

        return {'id_monitor': id_monitor, 'msg': 'Monitor atualizado com sucesso'}

    @staticmethod
    def delete_monitor(id_monitor):
        db.session.delete(UserHasMonitorBase.query.filter_by(Monitor_idMonitor=id_monitor).first())
        db.session.delete(MonitorModel.query.filter_by(idMonitor=id_monitor).first())
        db.session.commit()
        return {'msg': 'Monitor excluído com sucesso'}
