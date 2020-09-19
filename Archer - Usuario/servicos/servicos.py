from PyQt5.QtWidgets import QMainWindow
import servicos.servicos_inter, calcula.calc, litc.litc, externo.externo
import analistas.analistas, informacoes.informacoes, decisao.decisao, ping.ping
import main
import sys


class Servicos(QMainWindow, servicos.servicos_inter.Ui_MainWindow):
      def __init__(self, usuario, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btncalc.clicked.connect(self.calculadora)
            self.btnlitc.clicked.connect(self.litc)
            self.btnexterno.clicked.connect(self.externo)
            self.btnping.clicked.connect(self.ping)
            self.btnntcabertura.clicked.connect(self.decisao)
            self.btnconsultanalistas.clicked.connect(self.analistas)
            self.btninformacoes.clicked.connect(self.informacoes)
            self.btnsair.clicked.connect(self.saindo)
            self.user = usuario

      def voltar(self):
            self.origem = main.Main()
            self.origem.show()
            self.hide()

      def saindo(self):
            sys.exit()


      def calculadora(self):
            self.ca = calcula.calc.CalculadoraIp(self.user)
            self.ca.show()
            self.hide()

      def litc(self):
            self.li = litc.litc.Litc(self.user)
            self.li.show()
            self.hide()

      def externo(self):
            self.ex = externo.externo.Externo(self.user)
            self.ex.show()
            self.hide()

      def ping(self):
            self.ca = ping.ping.Ping(self.user)
            self.ca.show()
            self.hide()

      def decisao(self):
            self.ab = decisao.decisao.Decisao(self.user)
            self.ab.show()
            self.hide()

      def consultaportas(self):
            self.ca = calcula.calc.CalculadoraIp(self.user)
            self.ca.show()
            self.hide()

      def analistas(self):
            self.an = analistas.analistas.Analistas(self.user)
            self.an.show()
            self.hide()

      def informacoes(self):
            self.inf = informacoes.informacoes.Informacoes(self.user)
            self.inf.show()
            self.hide()
