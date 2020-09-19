from PyQt5.QtWidgets import QMainWindow, QDialog
import analistas.analistas_inter
from servicos import servicos
import sys


class Analistas(QMainWindow, analistas.analistas_inter.Ui_MainWindow, QDialog):
    def __init__(self, user, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnvoltarconsulta.clicked.connect(self.voltar)
            self.btnsairconsulta.clicked.connect(self.saindo)
            self.btnconsultar.clicked.connect(self.realizaronsulta)
            self.user = user

    def voltar(self):
            self.origem = servicos.Servicos(self.user)
            self.origem.show()
            self.hide()

    def saindo(self):
            sys.exit()


    def realizaronsulta(self):
        if self.vinhedo.isChecked():
            self.textBrowser.setText('Analista: João\n'
                                            'Ramal: 2675\n'
                                         'Celular: 0 98888-7777\n'
                                        'Email: scania@scania.com\n')





