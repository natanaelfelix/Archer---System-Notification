from PyQt5.QtWidgets import QMainWindow
import atualizarinfo.agendamento.agendamento
from msg.todas.ssbnaoencontrado import ssb_inter_erro


class Erro(QMainWindow, ssb_inter_erro.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnsair.clicked.connect(self.voltar)

            self.user = user

    def voltar(self):
        self.volta = atualizarinfo.agendamento.agendamento.Agendamento(self.user)
        self.volta.show()
        self.hide()






