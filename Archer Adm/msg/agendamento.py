from PyQt5.QtWidgets import QMainWindow
import atualizarinfo.agendamento.agendamento , servicos.servicos
from msg.todas.agendamento import agendamento_inter_erro


class Erro(QMainWindow, agendamento_inter_erro.Ui_MainWindow):
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
        self.volta = atualizarinfo.agendamento.agendamento.Agendamento(self.user)
        self.volta.show()
        self.hide()






