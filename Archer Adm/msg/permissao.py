from PyQt5.QtWidgets import QMainWindow
import servicos.servicos
from msg.todas.permissao import permissao_inter


class Erro(QMainWindow, permissao_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnsair.clicked.connect(self.voltar)

            self.user = user

    def voltar(self):
        self.volta = servicos.servicos.Servicos(self.user)
        self.volta.show()
        self.hide()






