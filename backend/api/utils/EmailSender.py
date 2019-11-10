import smtplib
from backend.api.utils import constants as const
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from backend.api.utils.errors import ReadExceptionSmtp


class Sender():
    def __init__(self, host=const.HOST_SMTP, port=const.HOST_PORT):
        self.server = smtplib.SMTP(host, port)
        self.msg = MIMEMultipart()

    def __del__(self):
        if self.server:
            self.server.quit()

    def set_login(self, email, passw):
        # Authentication Login
        # email: String, passw: String

        if email and passw:
            self.server.login(email, passw)

    def set_header(self, dest, frrom, subject):
        # Create Header
        # dest: List of String , frrom: String, subject: String

        self.frrom = frrom
        self.dest = dest
        self.msg['Subject'] = subject
        self.msg['From'] = frrom
        header_to = ", ".join(dest)
        self.msg['To'] = header_to

    def set_msg(self, mensg, type_msg):
        # Attach Content in Body Message
        # mensg: String/Html , type_msg: html/text

        body = MIMEText(mensg, type_msg)
        self.msg.attach(body)

    def set_attachment(self, pathfile=None):
        # Attachment file in email
        # pathfile: String

        if pathfile:
            with open(pathfile, "rb") as fo:
                arquivo_conteudo = MIMEApplication(fo.read())
                filename = pathfile.split('/')[-1]
                arquivo_conteudo.add_header('Content-Disposition', 'attachment', filename=filename)
                self.msg.attach(arquivo_conteudo)

    def send_message(self):
        try:
            self.server.sendmail(self.frrom, self.dest, self.msg.as_string())
            return {
                "sucesso": True,
                "mensagem": "Email enviado com sucesso!"
            }
        except Exception as e:
            raise ReadExceptionSmtp(message=e)
