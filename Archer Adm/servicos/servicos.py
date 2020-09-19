from PyQt5.QtWidgets import QMainWindow
import servicos.servicos_inter
import calcula.calc, disponibilidade.disponibilidade
import analistas.analistas, informacoes.informacoes, ping.ping, pymysql, msg.permissao, funcionalidade.banco.bd
from atualizarinfo import atualizar
from cadastro import cadastro
import main
import sys


class Servicos(QMainWindow, servicos.servicos_inter.Ui_MainWindow):
      def __init__(self, usuario, parent=None):
            super().__init__(parent)
            super().setupUi(self)

            self.btncalc.clicked.connect(self.calculadora)
            self.btnping.clicked.connect(self.ping)
            self.btnconsultanalistas.clicked.connect(self.analistas)
            self.btninformacoes.clicked.connect(self.informacoes)
            self.btnatualizar.clicked.connect(self.atualizar)
            self.btnsair.clicked.connect(self.saindo)
            self.btncadastrar.clicked.connect(self.cadastro)
            self.btnconsultaportas.clicked.connect(self.consultando)
            self.user = usuario

      def voltar(self):
            self.origem = main.Main()
            self.origem.show()
            self.hide()

      def saindo(self):
            sys.exit()


      def calculadora(self):
            self.ca = calc.CalculadoraIp(self.user)
            self.ca.show()
            self.hide()


      def ping(self):
            self.ca = ping.ping.Ping(self.user)
            self.ca.show()
            self.hide()


      def consultando(self):
            self.di = disponibilidade.disponibilidade.Disponibilidade(self.user)
            self.di.show()
            self.hide()

      def analistas(self):
            self.an = analistas.analistas.Analistas(self.user)
            self.an.show()
            self.hide()

      def informacoes(self):
            self.inf = informacoes.informacoes.Informacoes(self.user)
            self.inf.show()
            self.hide()

      def atualizar(self):
            resut = funcionalidade.banco.bd.Bd.permissao_consulta(self.user.emaillogon)
            try:
                if resut:
                    self.atu = atualizar.Atualizar(self.user)
                    self.atu.show()
                    self.hide()
                else:
                      self.err = msg.permissao.Erro(self.user)
                      self.err.show()
                      self.hide()
            except Exception as Error:
                  self.err = msg.permissao.Erro(self.user)
                  self.err.show()
                  self.hide()

      def cadastro(self):
            resut = funcionalidade.banco.bd.Bd.permissao_consulta(self.user.emaillogon)
            try:
                if resut == True:
                    self.cad = cadastro.Cadastro(self.user)
                    self.cad.show()
                    self.hide()
                else:
                      self.err = msg.permissao.Erro(self.user)
                      self.err.show()
                      self.hide()
            except Exception as Error:
                  self.err = msg.permissao.Erro(self.user)
                  self.err.show()
                  self.hide()


