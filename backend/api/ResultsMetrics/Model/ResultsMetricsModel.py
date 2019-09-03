from backend.api.model_base import ResultsMetricsBase
from backend import db


class ResultsMetricsModel(ResultsMetricsBase):

    def __call__(self, oximetry, heart, temperature, date_results, whm):
        self.base = ResultsMetricsBase(oximetry, heart, temperature, date_results, whm)

    @staticmethod
    def insert_results_metrics(self):
        db.session.add(self.base)
        db.session.commit()
