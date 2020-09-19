from PyQt5.QtWidgets import QMainWindow
import informacoes.info_inter
from servicos import servicos
from funcionalidade.banco import consulta
import sys


class Informacoes(QMainWindow, informacoes.info_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnsair.clicked.connect(self.saindo)
            self.btnvoltar.clicked.connect(self.voltar)
            self.btnconsultar.clicked.connect(self.consulta)
            self.user = user

    def voltar(self):
        self.volta = servicos.Servicos(self.user)
        self.volta.show()
        self.hide()

    def saindo(self):
            sys.exit()
    def consulta(self):
        if self.vivo.isChecked():
            escolha = 'Vivo'
            busca = consulta.ConsultaBanco(escolha)
            re = busca.busca()
            self.resultadoconsulta.setText((str(re)))
        elif self.embratel.isChecked():
            escolha = 'Embratel'
            busca = consulta.ConsultaBanco(escolha)
            re = busca.busca()
            self.resultadoconsulta.setText((str(re)))






