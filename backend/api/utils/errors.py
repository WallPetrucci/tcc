from backend.api.utils import constants as const


class ReadExceptionSmtp(Exception):
    def __init__(self,
                 message=const.ERROR_MESSAGE_EMAIL,
                 info=const.ERROR_INFO_EMAIL):
        Exception.__init__(self, f"{const.ERROR_SEND_MAIL} {message}")
        self.info = info
