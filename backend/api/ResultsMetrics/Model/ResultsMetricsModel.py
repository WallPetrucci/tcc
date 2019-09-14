from backend.api.model_base import ResultsMetricsBase
from backend import db
from datetime import datetime, timedelta
from backend.api.ResultsMetrics import constants as const


class ResultsMetricsModel(ResultsMetricsBase):

    def __init__(self, **kwargs):
        super(ResultsMetricsModel, self).__init__(**kwargs)

    def insert_results_metrics(self, list_objects):
        # db.session.
        # db.session.commit()
        db.engine.execute(self.__table__.insert(), list_objects)

    @staticmethod
    def get_result_metrics(id_user):
        today_date = datetime.now()

        database_result_metrics = db.session.query(
            ResultsMetricsModel.date_results,
            db.func.avg(ResultsMetricsModel.oximetry),
            db.func.avg(ResultsMetricsModel.heart),
            db.func.avg(ResultsMetricsModel.temperature)
        ).filter(
            ResultsMetricsModel.date_results.between(today_date - timedelta(days=const.RESULT_METRICS_DAY), today_date)
        ).filter_by(User_idUser=id_user).group_by(db.func.cast(ResultsMetricsModel.date_results, db.Date)).all()

        result_metrics = {'oximetry': [], 'heart': [], 'temperature': []}

        for result in database_result_metrics:
            result_metrics.get('oximetry').append({'data': result[0].strftime("%d-%m-%Y"), 'result': result[1]})
            result_metrics.get('heart').append({'data': result[0].strftime("%d-%m-%Y"), 'result': result[2]})
            result_metrics.get('temperature').append({'data': result[0].strftime("%d-%m-%Y"), 'result': result[3]})

        return result_metrics
