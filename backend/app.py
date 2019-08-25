from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from backend import constants as const
from backend.api.Alerts.Controller.AlertsController import AlertsController

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = const.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()

api.add_resource(AlertsController, '/alerts')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
