from backend import app, api

# Controllers Imports
from backend.api.Address.Controller.AddressController import AddressController
from backend.api.User.Controller.UserController import UserController
from backend.api.Alerts.Controller.AlertsController import AlertsController
from backend.api.Devices.Controller.DevicesController import DevicesController
from backend.api.Monitor.Controller.MonitorController import MonitorController
from backend.api.Monitor.Controller.MonitoringController import MonitoringController
from backend.api.RecoverPassword.Controller.RecoverPasswordController import RecoverPasswordController
from backend.api.ResultsMetrics.Controller.ResultsMetricsController import ResultsMetricsController
from backend.api.UserSettings.Controller.UserSettingsController import UserSettingsController
from backend.api.Login.Controller.LoginController import LoginController
from backend.api.HealthCheck import HealthCheck

# Locals Imports
import backend.constants as const

api.add_resource(AddressController, '/api/address/', '/api/address/<int:id_user>',
                 '/api/address/update/<int:id_Address>', '/api/address/delete/<int:id_Address>')
api.add_resource(AlertsController, '/api/alerts/<int:user_id>')
api.add_resource(DevicesController, '/api/devices/', '/api/devices/<int:user_id>')
api.add_resource(MonitorController, '/api/monitor/', '/api/monitor/<int:id>')
api.add_resource(MonitoringController, '/api/monitoring/')
api.add_resource(RecoverPasswordController, '/api/recoverpassword/')
api.add_resource(ResultsMetricsController, '/api/resultsmetrics/<int:id_user>', '/api/resultsmetrics/')
api.add_resource(HealthCheck, '/api/')
api.add_resource(UserController, '/api/user/', '/api/user/<int:id>')
api.add_resource(LoginController, '/api/login/')
api.add_resource(UserSettingsController, '/api/usersettings/', '/api/usersettings/<int:id_User>',
                 '/api/usersettings/update/<int:id_Settings>')

if __name__ == '__main__':
    app.run(debug=True,
            host=const.HOST_DEFAULT,
            port=const.PORT_DEFAULT)
