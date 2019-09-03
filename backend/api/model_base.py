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
    Sensor_idSensor = db.Column(db.Integer, db.ForeignKey('Sensor.idSensor'))

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

<<<<<<< Updated upstream
    def __init__(self, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)
=======
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone
>>>>>>> Stashed changes

    def __repr__(self):
        return "<Monitor%r>" % self.name


class RecoverPasswordBase(db.Model):

    __tablename__ = 'RecoverPassword'

    idRecoverPassoword = db.Column(db.Integer, primary_key=True)
    dateTime = db.Column(db.String(80))
    codeConfirm = db.Column(db.String(120))
    expiration = db.Column(db.String(120))
    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))
    User_Devices_idDevices = db.Column(db.Integer, db.ForeignKey('User.Devices_idDevices'))
    User_UserSettings_idUserSettings = db.Column(db.Integer, db.ForeignKey('User.UserSettings.idUserSettings'))

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
    User_Devices_idDevices = db.Column(db.Integer, db.ForeignKey('User.Devices_idDevices'))
    User_UserSettings_idUserSettings = db.Column(db.Integer, db.ForeignKey('User.UserSettings.idUserSettings'))

    def __init__(self, *args, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<ResultsMetrics%r>" % self.idResultsMetrics


class ResultsMetricsHasAlertsBase(db.Model):

    __tablename__ = 'ResultsMetrics_has_Alerts'

    ResultMetrics_idResultsMetrics = db.Column(db.Integer, db.ForeignKey('ResultsMetrics.idResultsMetrics'))
    ResultsMetrics_User_idUser = db.Column(db.Integer, db.ForeignKey('ResultsMetrics.User_idUSer'))
    ResultsMetrics_User_Devices_idDevices = db.Column(db.Integer,
                                                      db.ForeignKey('ResultsMetrics.User_Devices_idDevices'))

    ResultMetrics_User_UserSettings_idUserSettings = db.Column(
        db.Integer, db.ForeignKey('ResultsMetrics.User_UserSettings_idUserSettings'))

    Alerts_idAlerts = db.Column(db.Integer, db.ForeignKey('User.idUser'))
    sendAlert = db.Column(db.Integer, nullable=True)
    dateTimeLastSend = db.Column(db.DateTime(), nullable=True)

    def __init__(self, *args, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<ResultsMetricsHasAlerts%r>" % self.idResultsMetrics


class SensorBase(db.Model):

    __tablename__ = 'Sensor'

    idSensor = db.Column(db.Integer, primary_key=True)
    sensorType = db.Column(db.String(45))

    def __init__(self, *args, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<Sensor%r>" % self.idSensor


class UserBase(db.Model):

    __tablename__ = 'User'

    idUser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    dateBirth = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(10))
    cel = db.Column(db.String(15))
    Devices_idDevices = db.Column(db.Integer, db.ForeignKey('Devices.idDevices'))
    UserSettings_idUserSettings = db.Column(db.Integer, db.ForeignKey('UserSettings.idUserSettings'))
    Address_idAddress = db.Column(db.Integer, db.ForeignKey('Address.idAddress'))

<<<<<<< Updated upstream
=======
    # Devices = db.relationship('Devices', foreign_keys=Devices_idDevices)
    # UserSettings = db.relationship('UserSettings', foreign_keys=UserSettings_idUserSettings)
    # Address = db.relationship('Address', foreign_keys=Address_idAddress)

>>>>>>> Stashed changes
    def __init__(self, *args, **kwargs):
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

    def __init__(self, *args, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<UserSettings%r>" % self.idUserSettings


class UserHasMonitorBase(db.Model):

    __tablename__ = 'User_has_Monitor'

    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))
    User_Devices_idDevices = db.Column(db.Integer, db.ForeignKey('User.Devices_idDevices'))
    Monitor_idMonitor = db.Column(db.Integer, db.ForeignKey('Monitor.idMonitor'))
    token = db.Column(db.String(45), nullable=False)

    def __init__(self, *args, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<UserSettings%r>" % self.idUserSettings
