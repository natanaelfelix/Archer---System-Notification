from PyQt5.QtWidgets import QMainWindow
import litc.litc_inter, servicos.servicos, funcionalidade.email.envio, funcionalidade.email.corpo_email
import sys


class Litc(QMainWindow, litc.litc_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnsair.clicked.connect(self.saindo)
            self.btnvoltar.clicked.connect(self.voltar)
            self.btnenviar.clicked.connect(self.enviarmail)
            self.user = user


    def voltar(self):
        self.volta = servicos.servicos.Servicos(self.user)
        self.volta.show()
        self.hide()

    def saindo(self):
            sys.exit()

    def enviarmail(self):
        try:
            dest = self.inputdestinatario.text()
            copia = self.inputcopia.text()
            im = self.inputim.text()
            sw = self.inputsw.text()
            int = self.inputporta.text()
            opfp = self.inputoperadorfp.text()
            #obs = self.inputobservcoes.text()

            corpo = funcionalidade.email.corpo_email.Body.call_litc(sw, str(im), int, opfp)
            enviando = funcionalidade.email.envio.Envio(self.user.emaillogon, self.user.senhalogon, dest, corpo, copia)
            funcionalidade.email.envio.Envio.envio_email(enviando)



        except Exception as Error:

            print(Error)




