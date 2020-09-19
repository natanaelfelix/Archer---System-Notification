from PyQt5.QtWidgets import QMainWindow, QTextEdit
import externo.externo_inter
import servicos.servicos, funcionalidade.email.envio, funcionalidade.email.corpo_email
import sys


class Externo(QMainWindow, externo.externo_inter.Ui_MainWindow):
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
            sw = self.imputsw.text()
            op = self.imputoperadora.text()
            inte = self.inputporta.text()
            lo = self.inputlocalidade
            opfp = self.inputoperadorfp.text()
            #obs = self.inputobservcoes.setText()
            #print(obs)
            corpo = funcionalidade.email.corpo_email.Body.call_externo(op, lo, sw, inte, im, opfp)
            enviando = funcionalidade.email.envio.Envio(self.user.emaillogon, self.user.senhalogon, dest, corpo, copia)
            funcionalidade.email.envio.Envio.envio_email(enviando)



        except Exception as Error:

            print(Error)





