from backend import db


class AlertsBase(db.Model):

    __tablename__ = 'Alerts'

    idAlerts = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.String(100), nullable=True)
    typeAlerts = db.Column(db.String(45), nullable=True)

    def __init__(self, idAlerts, messages, typeAlerts):
        self.idAlerts = idAlerts
        self.messages = messages
        self.typeAlerts = typeAlerts

    def __repr__(self):
        return "<Alerts%r>" % self.idAlerts


class DevicesBase(db.Model):

    __tablename__ = 'Devices'

    idDevices = db.Column(db.Integer, primary_key=True)
    idHardware = db.Column(db.String(255))
    Sensor_idSensor = db.Column(db.Integer, db.ForeignKey('Sensor.idSensor'))
    Sensor = db.relationship('SensorBase', foreign_keys=Sensor_idSensor)

    # def __init__(self, idDevices, idHardware, Sensor_idSensor):
    #     self.idDevices = idDevices
    #     self.idHardware = idHardware
    #     self.Sensor_idSensor = Sensor_idSensor

    # def __repr__(self):
    #     return "<Devices%r>" % self.idDevices



class MonitorBase(db.Model):

    __tablename__ = 'Monitor'

    idMonitor = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    cel = db.Column(db.String(45))

    def __init__(self, name, email, cel):
        self.name = name
        self.email = email
        self.cel = cel

    def __repr__(self):
        return "<Monitor%r>" % self.name


class RecoverPasswordBase(db.Model):

    __tablename__ = 'RecoverPassword'

    idRecoverPassoword = db.Column(db.Integer, primary_key=True)
    dateTime = db.Column(db.String(80))
    codeConfirm = db.Column(db.String(120))
    expiration = db.Column(db.String(120))
    User_idUser = db.Column(db.Integer, db.ForeignKey('User.idUser'))
    User_Devices_idDevices = db.Column(db.Integer, db.ForeignKey('Sensor.idSensor'))
    User_UserSettings_idUserSettings = db.Column(db.Integer, db.ForeignKey('Sensor.idSensor'))

    def __init__(self, **kwargs):

        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<RecoverPassword%r>" % self.idRecoverPassoword


class ResultMetricsBase(db.Model):
    idResultsMetrics = db.Column(db.Integer, primary_key=True)
    oximetry = db.Column(db.String(45))
    heart = db.Column(db.String(45))
    heart = db.Column(db.String(45))
    date_results = db.Column(db.DateTime())
    User_idUSer = db.Column(db.Integer)
    User_Devices_idDevices = db.Column(db.Integer)
    User_UserSettings_idUserSettings = db.Column(db.Integer)


class SensorBase(db.Model):

    __tablename__ = 'Sensor'


    idSensor = db.Column(db.Integer, primary_key=True)
    sensorType = db.Column(db.String(45))

    def __init__(self, idSensor, sensorType):
        self.idSensor = idSensor
        self.sensorType = sensorType

    def __repr__(self):
        return "<Monitor%r>" % self.idSensor


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


    # Devices = db.relationship('Devices', foreign_keys=Devices_idDevices)
    # UserSettings = db.relationship('UserSettings', foreign_keys=UserSettings_idUserSettings)
    # Address = db.relationship('Address', foreign_keys=Address_idAddress)

    def __init__(self, *args, **kwargs):
        for (attr_name, value) in kwargs.items():
            setattr(self, attr_name, value)

    def __repr__(self):
        return "<User%r>" % self.name


class UserSettingsBase(db.Model):
    idUserSettings = db.Column(db.Integer, primary_key=True)
    heartRate = db.Column(db.JSON, nullable=False)
    oximetry = db.Column(db.String(120), nullable=False)
    temperature = db.Column(db.String(120), nullable=False)
    acitveAlertOximetry = db.Column(db.String(120), nullable=False)
    activeAlertHeartRate = db.Column(db.String(120), nullable=False)
    activeAlertBTemperature = db.Column(db.String(120), nullable=False)
