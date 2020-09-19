from PyQt5.QtWidgets import QMainWindow
import informacoes.informacoes
from msg.todas.consulta import consulta_inter_erro


class Erro(QMainWindow, consulta_inter_erro.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnsair.clicked.connect(self.voltar)
            self.user = user

    def voltar(self):
        self.volta = informacoes.informacoes.Informacoes(self.user)
        self.volta.show()
        self.hide()






