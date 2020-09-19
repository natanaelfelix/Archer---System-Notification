from PyQt5.QtWidgets import QMainWindow
import servicos.servicos, atualizarinfo.informacoesdiversas.informacoes
from msg.todas.aualizando_inserindo import atualiza_inter_erro
from msg.todas.aualizando_inserindo.erro import inserir_inter_erro


class Sucesso(QMainWindow, atualiza_inter_erro.Ui_MainWindow):
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
        self.novo = atualizarinfo.informacoesdiversas.informacoes.Informacoes(self.user)
        self.novo.show()
        self.hide()


class Erro(QMainWindow, inserir_inter_erro.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnok.clicked.connect(self.voltar)
            self.user = user

    def voltar(self):
        self.novo = atualizarinfo.informacoesdiversas.informacoes.Informacoes(self.user)
        self.novo.show()
        self.hide()



