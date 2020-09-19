from PyQt5.QtWidgets import QMainWindow
import informacoes.info_inter, msg.consulta_erro
from servicos import servicos
from funcionalidade.banco import bd
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
        try:
            pedido = self.inputinfo.text()
            resu = bd.Bd.consulta(pedido)
            lista = resu
            if type(list(resu)):
                self.resultadoconsulta.setText(" " .join(lista))
            else:
                self.resultadoconsulta.setText(resu)
        except Exception as Error:
              self.err = msg.consulta_erro.Erro(self.user)
              self.err.show()
              self.close()









