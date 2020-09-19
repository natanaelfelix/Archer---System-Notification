from PyQt5.QtWidgets import QApplication, QMainWindow
from login import login_inter, valida_login
from servicos import servicos
import sys


class Main(QMainWindow, login_inter.Ui_MainWindow):
      def __init__(self, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btnlogin.clicked.connect(self.logar)
            self.btnsair.clicked.connect(self.saindo)

      def logar(self):
            em = self.inputemail.text()
            sh = self.inputsenha.text()
            self.user = valida_login.Login(em, sh)
            self.proxjan = servicos.Servicos(self.user)
            self.proxjan.show()
            self.hide()

      @staticmethod
      def saindo():
            sys.exit()


if __name__ == '__main__':
      qt= QApplication(sys.argv)
      ma = Main()
      ma.show()
      qt.exec_()
