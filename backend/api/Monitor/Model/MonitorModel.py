from backend.api.model_base import MonitorBase, UserHasMonitorBase
from backend.api.User.Model.UserModel import UserModel
from backend.api.Devices.Model.DevicesModel import DevicesModel
from backend.api.utils.EmailSender import Sender
from backend.api.utils import constants as const_email
from backend import db
import random
import string


class MonitorModel(MonitorBase):

    def __init__(self, **kwargs):
        super(MonitorModel, self).__init__(**kwargs)

    def insert_monitor(self, id_user):
        db.session.add(self)
        db.session.commit()

        token = "{}{}{}".format(id_user, ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
                                self.idMonitor)

        user_has_monitor = UserHasMonitorBase(User_idUser=id_user, Monitor_idMonitor=self.idMonitor, token=token)
        user = UserModel.query.filter_by(idUser=id_user).first()
        email_sender = Sender()
        email_sender.set_header([self.email], const_email.EMAIL_DEST, const_email.SUBJECT)
        email_sender.set_msg(const_email.MONITOR.format(self.name, user.name, token), 'html')
        email_sender.send_message()
        db.session.add(user_has_monitor)
        db.session.commit()

        return {'id_monitor': self.idMonitor, 'token': token}

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

    @staticmethod
    def monitoring(token):
        result = UserHasMonitorBase.query.add_columns(
            UserModel.name.label('name'), UserModel.email.label('email'),
            UserModel.cel.label('cel'), UserModel.dateBirth.label('date_birth'),
            DevicesModel.idHardware.label('whmid')
        ).join(MonitorModel).join(UserModel).join(DevicesModel).filter(UserHasMonitorBase.token == token).first()

        if result:
            data_monitoring = {
                'user_name': result.name,
                'user_email': result.email,
                'cel': result.cel,
                'date_birth': result.date_birth.strftime("%d/%m/%Y"),
                'device_id': result.whmid
            }
            return data_monitoring
        return {'msg': 'Não há monitor cadastrado com esse token'}
