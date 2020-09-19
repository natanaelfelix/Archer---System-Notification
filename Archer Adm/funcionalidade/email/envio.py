from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


class Envio:
    def __init__(self, email, senha, destinatario, corpo, copia=None):
        self.email = email
        self.senha = senha
        self.copia = copia
        self.destinatario = destinatario
        self.corpo = corpo


    def envio_email(self):

        msg = MIMEMultipart()
        msg['from'] = str(self.email)
        msg['to'] = str(self.destinatario)
        msg['Co'] = str(self.copia)
        msg['subject'] = str('Notificação Archer')
        msg.attach(MIMEText(self.corpo))

        with smtplib.SMTP(host='smtp.live.com', port=25) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(self.email, self.senha)
            smtp.send_message(msg)
            print('Email enviado com sucesso')

