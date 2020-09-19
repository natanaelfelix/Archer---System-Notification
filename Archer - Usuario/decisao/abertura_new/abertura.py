from PyQt5.QtWidgets import QMainWindow
import decisao.abertura_new.abertura_inter
import servicos.servicos, funcionalidade.email.envio, funcionalidade.email.corpo_email
import sys


class Abertura(QMainWindow, decisao.abertura_new.abertura_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnvoltar.clicked.connect(self.voltar)
            self.btnsair.clicked.connect(self.saindo)
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
            opfp = self.inputoperadorfp.text()
            an = self.inputanalistalocal.text()
            ptr = self.inputprotocolo.text()
            hr = self.inputvisita.text()
            op = self.inputoperadoralink.text()
            lo = self.inputlocal.text()
            #obs = self.inputobservcoes.text()

            corpo = funcionalidade.email.corpo_email.Body.notificar_nova_abertura(op, im, lo, ptr, hr, an, opfp)
            enviando = funcionalidade.email.envio.Envio(self.user.emaillogon, self.user.senhalogon, dest, corpo, copia)
            funcionalidade.email.envio.Envio.envio_email(enviando)
            sh = self.sucesso.setText('E-mail enviado com sucesso!\n'
                                      'Não se esqueça de atualizar\n '
                                      'o time sobre o chamado.')
        except Exception as Error:

            print(Error)
