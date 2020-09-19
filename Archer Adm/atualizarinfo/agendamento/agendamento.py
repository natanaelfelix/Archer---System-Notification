from PyQt5.QtWidgets import QMainWindow, QWidget
import atualizarinfo.agendamento.agendamento_inter, funcionalidade.banco.bd, msg.ssberro
from analistas import analistas
from servicos import servicos
import sys


class Agendamento(QMainWindow, atualizarinfo.agendamento.agendamento_inter.Ui_MainWindow, QWidget):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnvoltar.clicked.connect(self.voltar)
            self.btnsair.clicked.connect(self.saindo)
            self.btnconsulta.clicked.connect(self.consulta)
            self.btnbuscar.clicked.connect(self.busca)
            self.user = user

    def voltar(self):
            self.origem = servicos.Servicos(self.user)
            self.origem.show()
            self.hide()

    def saindo(self):
            sys.exit()

    def consulta(self):
            self.origem = analistas.Analistas(self.user)
            self.origem.show()
            self.hide()

    def busca(self):
        try:
            analista = self.inputssb.text()
            resu = funcionalidade.banco.bd.Bd.agendamento_busca(analista)
            if resu:
                self.result.setText(str(resu[0]) + str(resu[1]))
            else:
                self.ssb_erro = msg.ssberro.Erro(self.user)
                self.ssb_erro.show()
                self.hide()
        except Exception as Error:
            return self.result.setText(Error)







