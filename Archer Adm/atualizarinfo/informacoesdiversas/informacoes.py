from PyQt5.QtWidgets import QMainWindow
import msg.atualizando_inserindo, funcionalidade
from atualizarinfo.informacoesdiversas import infodiversas_inter
from informacoes import informacoes
from servicos import servicos
import sys


class Informacoes(QMainWindow, infodiversas_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnvoltar.clicked.connect(self.voltar)
            self.btnsair.clicked.connect(self.saindo)
            self.btnconsulta.clicked.connect(self.consulta)
            self.btnatuali.clicked.connect(self.atualizar_inserir)

            self.user = user

    def voltar(self):
            self.origem = servicos.Servicos(self.user)
            self.origem.show()
            self.hide()

    def saindo(self):
            sys.exit()

    def consulta(self):
            self.origem = informacoes.Informacoes(self.user)
            self.origem.show()
            self.hide()

    def atualizar_inserir(self):
        try:
            servi = self.inputnovoserv.text()
            cont = self.inputinfo.toPlainText()
            if servi or cont:
                inserindo = funcionalidade.banco.bd.Bd.atualizar_inserir_infos(servi, cont)
                if inserindo:
                    self.msg = msg.atualizando_inserindo.Sucesso(self.user)
                    self.msg.show()
                    self.hide()
            else:
                raise ValueError('Deu ruim')

        except Exception as Error:
            self.er = msg.atualizando_inserindo.Erro(self.user)
            self.er.show()
            self.hide()







