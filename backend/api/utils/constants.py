HOST_SMTP = 'aspmx.l.google.com'
HOST_PORT = 25
USER_EMAIL = 'whmtccemail@gmail.com'
ERROR_BLANK_MSG = "Mensagem está em branco"
SUBJECT = "WHM"
EMAIL_DEST = "whmtccemail@gmail.com"

ERROR_SEND_MAIL = "Error Send Email: "
ERROR_MESSAGE_EMAIL = "Email, was not sent successfully"
ERROR_INFO_EMAIL = "Error sender"
EMAIL_TEMPLATE = """<body>
                        Olá, identificamos uma anormalidade seus dados de {}.
                        Estamos disparando esse alerta de {} para que você possa providenciar atendimento !
                    <body>"""
RECOVERY = """<body>Olá, recebemos sua solicitação de recuperação de senha, e viemos informá-la: {}!<body>"""
MONITOR = """<body>
                        Olá {}, somos da WHM. O usuário {} solicitou que você monitore os sinais vitais dele.
                        Para começar a monitorar, basta <a href='http://localhost:8080/monitoring/{}'>clicar aqui</a>!
                    <body>"""

RESULT_METRICS_DAY = 30

