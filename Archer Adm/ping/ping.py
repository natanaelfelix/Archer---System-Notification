from PyQt5.QtWidgets import QMainWindow
import ping.ping_inter
import servicos.servicos, funcionalidade.ping.ping
import sys


class Ping(QMainWindow, ping.ping_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnsair.clicked.connect(self.saindo)
            self.btnvoltar.clicked.connect(self.voltar)
            self.btnping.clicked.connect(self.pingar)
            self.user = user

    def voltar(self):
        self.volta = servicos.servicos.Servicos(self.user)
        self.volta.show()
        self.hide()

    def saindo(self):
            sys.exit()

    def pingar(self):
        host = self.inputipping.text()
        pi = funcionalidade.ping.ping.Pingando(host)
        resutado = pi.realizarping()
        self.jaenlaresult.setText(str(resutado))




