from PyQt5.QtWidgets import QMainWindow
from calcula import calc_inter
from servicos import servicos
from calcula.calculadora_ip_cont import main
import sys


class CalculadoraIp(QMainWindow, calc_inter.Ui_MainWindow):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btncalcip.clicked.connect(self.realizaronsulta)
            self.btnvoltar.clicked.connect(self.voltar)
            self.btnsair.clicked.connect(self.saindo)
            self.ip = self.inputip
            self.cid = self.inputcidr
            self.user = user

    def voltar(self):
        self.volta = servicos.Servicos(self.user)
        self.volta.show()
        self.hide()

    def saindo(self):
            sys.exit()

    def realizaronsulta(self):

        ip = self.ip.text()
        cidr = self.cid.text()
        calc = main.CalculandoTudo(ip, cidr)
        try:
            resutado = calc.verifica()
            self.jaenlaresult.setText(str(resutado))

        except Exception as Error:

            self.jaenlaresult.setText(str(Error))


