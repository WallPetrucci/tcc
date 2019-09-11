from backend.api.model_base import ResultsMetricsBase
from backend import db


class ResultsMetricsModel(ResultsMetricsBase):

    def __init__(self, **kwargs):
        super(ResultsMetricsModel, self).__init__(**kwargs)

    def insert_results_metrics(self, list_objects):
        # db.session.
        # db.session.commit()
        db.engine.execute(self.__table__.insert(), list_objects)
