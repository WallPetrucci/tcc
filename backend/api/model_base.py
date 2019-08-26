from backend.database import DataBase

db = DataBase()


class AlertsBase(db.Model):
    idAlerts = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.String(100))
    typeAlerts = db.Column(db.String(45))


class DevicesBase(db.Model):
    idDevices = db.Column(db.Integer, primary_key=True)
    idHardware = db.Column(db.String(255))
    Sensor_idSensor = db.Column(db.Integer)


class MonitorBase(db.Model):
    idMonitor = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    cel = db.Column(db.String(45))


class RecoverPasswordBase(db.Model):
    idRecoverPassoword = db.Column(db.Integer, primary_key=True)
    dateTime = db.Column(db.String(80))
    codeConfirm = db.Column(db.String(120))
    expiration = db.Column(db.String(120))
    User_idUser = db.Column(db.Integer)
    User_Devices_idDevices = db.Column(db.Integer)
    User_UserSettings_idUserSettings = db.Column(db.Integer)


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
    idSensor = db.Column(db.Integer)
    sensorType = db.Column(db.String(45))


class UserBase(db.Model):
    idUser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    dateBirth = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(10))
    cel = db.Column(db.String(15))
    Devices_idDevices = db.Column(db.Integer)
    UserSettings_idUserSettings = db.Column(db.Integer)
    Address_idAddress = db.Column(db.Integer)


class UserSettingsBase(db.Model):
    my_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
