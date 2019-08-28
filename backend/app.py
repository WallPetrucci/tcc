from backend import app, api

# Controllers Imports
from backend.api.User.Controller.UserController import UserController
from backend.api.Alerts.Controller.AlertsController import AlertsController
from backend.api.Devices.Controller.DevicesController import DevicesController
from backend.api.Monitor.Controller.MonitorController import MonitorController
from backend.api.RecoverPassword.Controller.RecoverPasswordController import RecoverPasswordController
from backend.api.ResultsMetrics.Controller.ResultsMetricsController import ResultsMetricsController
from backend.api.Sensor.Controller.SensorController import SensorController
from backend.api.UserSettings.Controller.UserSettingsController import UserSettingsController
from backend.api.HealthCheck import HealthCheck

# Locals Imports
import backend.constants as const

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
