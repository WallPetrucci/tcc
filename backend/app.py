# Packages Imports
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Controllers Imports
from api.User.Controller.UserController import UserController
from api.Alerts.Controller.AlertsController import AlertsController
from api.Devices.Controller.DevicesController import DevicesController
from api.Monitor.Controller.MonitorController import MonitorController
from api.RecoverPassword.Controller.RecoverPasswordController import RecoverPasswordController
from api.ResultsMetrics.Controller.ResultsMetricsController import ResultsMetricsController
from api.Sensor.Controller.SensorController import SensorController
from api.UserSettings.Controller.UserSettingsController import UserSettingsController
from api.HealthCheck import HealthCheck

# Locals Imports
import constants as const
import config as conf


app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(AlertsController, '/api/alerts/')
api.add_resource(DevicesController, '/api/devices/')
api.add_resource(MonitorController, '/api/monitor/')
api.add_resource(RecoverPasswordController, '/api/recoverpassword/')
api.add_resource(ResultsMetricsController, '/api/resultsmetrics/')
api.add_resource(SensorController, '/api/sensor/')
api.add_resource(HealthCheck, '/api/')
api.add_resource(UserController, '/api/user/', '/api/user/<int:id_cliente>')
api.add_resource(UserSettingsController, '/api/usersettings/')

if __name__ == '__main__':
    app.run(debug=False,
            host=const.HOST_DEFAULT,
            port=const.PORT_DEFAULT)
    app.config['SQLALCHEMY_DATABASE_URI'] = conf.CONNECT_DB
    global db
    db = SQLAlchemy(app)
