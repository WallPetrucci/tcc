from backend.api.model_base import ResultsMetricsBase
from backend import db


class ResultsMetricsModel(ResultsMetricsBase):

    def __init__(self, oximetry, heart, temperature, date_results, User_idUser):
        self.base = ResultsMetricsBase(oximetry, heart, temperature, date_results, User_idUser)

    def insert_results_metrics(self):
        db.session.add(self.base)
        db.session.commit()
