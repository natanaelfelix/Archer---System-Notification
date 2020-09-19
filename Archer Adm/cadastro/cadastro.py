from PyQt5.QtWidgets import QMainWindow
import cadastro.cadastros_inter, msg.cadastro
from funcionalidade.banco import bd
from servicos import servicos
import sys


class Cadastro(QMainWindow, cadastro.cadastros_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnsair.clicked.connect(self.saindo)
            self.btnvoltar.clicked.connect(self.voltar)
            self.btncadastrar.clicked.connect(self.enviar)
            self.user = user

    def voltar(self):
        self.volta = servicos.Servicos(self.user)
        self.volta.show()
        self.hide()

    def saindo(self):
            sys.exit()

    def enviar(self):
        try:
            nome = self.inputnome.text()
            ssb = self.inputssb.text()
            area = self.inputarea.text()
            email = self.inputemail.text()
            contato = self.inputcontato.text()
            lider = self.inputlider.text()
            local = self.inputlocalidade.text()
            corpo = bd.Bd.cadastro_analistas(ssb, nome, area, lider, contato, email, local)
            self.err = msg.cadastro.Erro(self.user)
            self.err.show()
            self.hide()
        except Exception as Error:
            print(Error)






