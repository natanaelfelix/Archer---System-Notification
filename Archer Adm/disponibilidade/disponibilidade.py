from PyQt5.QtWidgets import QMainWindow
from disponibilidade import disponibilidade_inter
import servicos.servicos
import sys


class Disponibilidade(QMainWindow, disponibilidade_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnsair.clicked.connect(self.saindo)
            self.btnvoltar.clicked.connect(self.voltar)
            self.user = user

    def voltar(self):
        self.volta = servicos.servicos.Servicos(self.user)
        self.volta.show()
        self.hide()

    def saindo(self):
            sys.exit()





