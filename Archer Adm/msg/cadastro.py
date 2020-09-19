from PyQt5.QtWidgets import QMainWindow
import cadastro.cadastro , servicos.servicos
from msg.todas.cadastro import cadastro_inter_erro


class Erro(QMainWindow, cadastro_inter_erro.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnsair.clicked.connect(self.voltar)
            self.tbnovo.clicked.connect(self.novo)
            self.user = user

    def voltar(self):
        self.volta = servicos.servicos.Servicos(self.user)
        self.volta.show()
        self.hide()

    def novo(self):
        self.volta = cadastro.cadastro.Cadastro(self.user)
        self.volta.show()
        self.hide()






