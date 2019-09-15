from backend.api.model_base import MonitorBase, UserHasMonitorBase
from backend import db


class MonitorModel(MonitorBase):

    def __init__(self, **kwargs):
        super(MonitorModel, self).__init__(**kwargs)

    def insert_monitor(self, id_user):
        db.session.add(self)
        db.session.commit()

        user_has_monitor = UserHasMonitorBase(User_idUser=id_user, Monitor_idMonitor=self.idMonitor)
        db.session.add(user_has_monitor)
        db.session.commit()

        return {'id_monitor': self.idMonitor}

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
