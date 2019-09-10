from backend import db


class AddressBase(db.Model):
    __tablename__ = 'Address'

    idAddress = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(100), nullable=True)
    number = db.Column(db.String(45), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    neighborhood = db.Column(db.String(100), nullable=True)
    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))

    def __init__(self, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<Address%r>" % self.idAddress


class AlertsBase(db.Model):

    __tablename__ = 'Alerts'

    idAlerts = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.String(100), nullable=True)
    typeAlerts = db.Column(db.String(45), nullable=True)

    def __init__(self, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<Alerts%r>" % self.idAlerts


class DevicesBase(db.Model):

    __tablename__ = 'Devices'

    idDevices = db.Column(db.Integer, primary_key=True)
    idHardware = db.Column(db.String(255))
    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))

    def __init__(self, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<Devices%r>" % self.idDevices


class MonitorBase(db.Model):

    __tablename__ = 'Monitor'

    idMonitor = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    telephone = db.Column(db.String(45))

    def __init__(self, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<Monitor%r>" % self.name


class RecoverPasswordBase(db.Model):

    __tablename__ = 'RecoverPassword'

    idRecoverPassoword = db.Column(db.Integer, primary_key=True)
    dateTime = db.Column(db.String(80))
    codeConfirm = db.Column(db.String(120))
    expiration = db.Column(db.String(120))
    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))

    def __init__(self, **kwargs):

        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<RecoverPassword%r>" % self.idRecoverPassoword


class ResultsMetricsBase(db.Model):

    __tablename__ = 'ResultsMetrics'

    idResultsMetrics = db.Column(db.Integer, primary_key=True)
    oximetry = db.Column(db.String(45), nullable=True)
    heart = db.Column(db.String(45), nullable=True)
    temperature = db.Column(db.String(45), nullable=True)
    date_results = db.Column(db.DateTime(), nullable=True)
    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))

    def __init__(self, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<ResultsMetrics%r>" % self.idResultsMetrics


class ResultsMetricsHasAlertsBase(db.Model):

    __tablename__ = 'ResultsMetrics_has_Alerts'

    IdResultsMetrics_has_Alerts = db.Column(db.Integer, db.ForeignKey(
        'ResultsMetrics.idResultsMetrics'), primary_key=True)
    ResultsMetrics_idResultsMetrics = db.Column(db.Integer, db.ForeignKey('ResultsMetrics.idResultsMetrics'))
    ResultsMetrics_User_idUser = db.Column(db.Integer, db.ForeignKey('ResultsMetrics.User_idUser'))
    Alerts_idAlerts = db.Column(db.Integer, db.ForeignKey('User.idUser'))

    def __init__(self, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<ResultsMetricsHasAlerts%r>" % self.idResultsMetrics


class UserBase(db.Model):

    __tablename__ = 'User'

    idUser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    dateBirth = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(10))
    cel = db.Column(db.String(15))

    def __init__(self, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<User%r>" % self.name


class UserSettingsBase(db.Model):

    __tablename__ = 'UserSettings'

    idUserSettings = db.Column(db.Integer, primary_key=True)
    heartRate = db.Column(db.JSON, nullable=False)
    oximetry = db.Column(db.JSON, nullable=False)
    temperature = db.Column(db.JSON, nullable=False)
    acitveAlertOximetry = db.Column(db.Integer, nullable=False)
    activeAlertHeartRate = db.Column(db.Integer, nullable=False)
    activeAlertBTemperature = db.Column(db.Integer, nullable=False)
    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))

    def __init__(self, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<UserSettings%r>" % self.idUserSettings


class UserHasMonitorBase(db.Model):

    __tablename__ = 'User_has_Monitor'

    IdUser_has_Monitor = db.Column(db.Integer, primary_key=True)
    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))
    Monitor_idMonitor = db.Column(db.Integer, db.ForeignKey('Monitor.idMonitor'))

    def __init__(self, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<UserSettings%r>" % self.idUserSettings
