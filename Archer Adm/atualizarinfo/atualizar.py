from PyQt5.QtWidgets import QMainWindow
from atualizarinfo.agendamento import agendamento
from atualizarinfo.informacoesdiversas import informacoes
from atualizarinfo import atualizar_inter
from servicos import servicos
import sys


class Atualizar(QMainWindow, atualizar_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnatualizar.clicked.connect(self.informacoes_diversas)
            self.btnvoltar.clicked.connect(self.voltar)
            self.btnsair.clicked.connect(self.saindo)
            self.btnatualizaragenda.clicked.connect(self.atualizar_inserir)
            self.user = user


    def voltar(self):
        self.volta = servicos.Servicos(self.user)
        self.volta.show()
        self.hide()

    def saindo(self):
            sys.exit()

    def atualizar_inserir(self):
        self.ag = agendamento.Agendamento(self.user)
        self.ag.show()
        self.hide()

    def informacoes_diversas(self):
        self.ag = informacoes.Informacoes(self.user)
        self.ag.show()
        self.hide()



