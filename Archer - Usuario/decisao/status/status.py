from PyQt5.QtWidgets import QMainWindow
import decisao.status.status_inter
from servicos import servicos
import funcionalidade.email.envio, funcionalidade.email.corpo_email
import sys


class StatusChamado(QMainWindow, decisao.status.status_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnvoltar.clicked.connect(self.voltar)
            self.btnsair.clicked.connect(self.saindo)
            #self.btnenviar.clicked.connect(self.enviar)
            self.user = user


    def voltar(self):
        self.volta = servicos.Servicos(self.user)
        self.volta.show()
        self.hide()

    def saindo(self):
           sys.exit()

    def enviarmail(self):
        try:
            dest = self.inputdestinatario.text()
            copia = self.inputcopia.text()
            im = self.inputim.text()
            opfp = self.inputoperadorfp.text()
            an = self.inputanalistalocal.text()
            ptr = self.inputprotocolo
            op = self.inputoperadoralink
            #obs = self.inputobservcoes.text()

            corpo = funcionalidade.email.corpo_email.Body.status_com_analistas(op, im, ptr, an, opfp)
            enviando = funcionalidade.email.envio.Envio(self.user.emaillogon, self.user.senhalogon, dest, corpo, copia)
            funcionalidade.email.envio.Envio.envio_email(enviando)

        except Exception as Error:

           print(Error)
