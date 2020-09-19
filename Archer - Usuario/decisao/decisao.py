from PyQt5.QtWidgets import QMainWindow
from decisao.abertura_new import abertura
from decisao.status import status
import decisao.decisaoabertura_inter
from servicos import servicos
import sys


class Decisao(QMainWindow, decisao.decisaoabertura_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnconsultaranalistas.clicked.connect(self.status)
            self.btnabertura.clicked.connect(self.ntf_abertura)
            self.btnsairstauschamado.clicked.connect(self.saindo)
            self.btnvoltar.clicked.connect(self.voltar)
            self.user = user


    def voltar(self):
        self.volta = servicos.Servicos(self.user)
        self.volta.show()
        self.hide()

    def saindo(self):
            sys.exit()

    def ntf_abertura(self):
        self.na = abertura.Abertura(self.user)
        self.na.show()
        self.hide()

    def status(self):
        self.ne = status.StatusChamado(self.user)
        self.ne.show()
        self.hide()



