# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servicos_inter.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 431, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 410, 171, 71))
        self.label_2.setStyleSheet("image: url(:/servicosdoc/scania-logo-2.png);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 90, 101, 31))
        self.label_4.setObjectName("label_4")
        self.btnsair = QtWidgets.QPushButton(self.centralwidget)
        self.btnsair.setGeometry(QtCore.QRect(630, 460, 93, 28))
        self.btnsair.setObjectName("btnsair")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(470, 140, 291, 241))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnntcabertura = QtWidgets.QPushButton(self.widget)
        self.btnntcabertura.setObjectName("btnntcabertura")
        self.verticalLayout.addWidget(self.btnntcabertura)
        self.btnconsultaportas = QtWidgets.QPushButton(self.widget)
        self.btnconsultaportas.setObjectName("btnconsultaportas")
        self.verticalLayout.addWidget(self.btnconsultaportas)
        self.btnconsultanalistas = QtWidgets.QPushButton(self.widget)
        self.btnconsultanalistas.setObjectName("btnconsultanalistas")
        self.verticalLayout.addWidget(self.btnconsultanalistas)
        self.btninformacoes = QtWidgets.QPushButton(self.widget)
        self.btninformacoes.setObjectName("btninformacoes")
        self.verticalLayout.addWidget(self.btninformacoes)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(400, 150, 71, 221))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setStyleSheet("image: url(:/servicosdoc/1827402.png);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setStyleSheet("image: url(:/servicosdoc/418414.png);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setStyleSheet("image: url(:/servicosdoc/275376.png);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setStyleSheet("image: url(:/servicosdoc/information-160885_960_720.png);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(90, 140, 291, 241))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btncalc = QtWidgets.QPushButton(self.widget2)
        self.btncalc.setObjectName("btncalc")
        self.verticalLayout_3.addWidget(self.btncalc)
        self.btnlitc = QtWidgets.QPushButton(self.widget2)
        self.btnlitc.setObjectName("btnlitc")
        self.verticalLayout_3.addWidget(self.btnlitc)
        self.btnexterno = QtWidgets.QPushButton(self.widget2)
        self.btnexterno.setObjectName("btnexterno")
        self.verticalLayout_3.addWidget(self.btnexterno)
        self.btnping = QtWidgets.QPushButton(self.widget2)
        self.btnping.setObjectName("btnping")
        self.verticalLayout_3.addWidget(self.btnping)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(20, 150, 61, 221))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget3)
        self.label_3.setStyleSheet("image: url(:/servicosdoc/736663fe6f9e03fcb39ace9020c42b4c---cone-estacion--rio-de-calculadora-by-vexels.png);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_9 = QtWidgets.QLabel(self.widget3)
        self.label_9.setStyleSheet("image: url(:/servicosdoc/alerta.png);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.widget3)
        self.label_8.setStyleSheet("image: url(:/servicosdoc/ava.png);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.widget3)
        self.label_7.setStyleSheet("image: url(:/servicosdoc/ping-logo-png-transparent-svg-vector-freebie-supply-ping-png-2400_2400.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archer 1.0 - Serviços"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Archer -Sistema de notificações urgentes</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Serviços</span></p></body></html>"))
        self.btnsair.setText(_translate("MainWindow", "Sair"))
        self.btnntcabertura.setText(_translate("MainWindow", "Notificação de abertura de chamados"))
        self.btnconsultaportas.setText(_translate("MainWindow", "Consulta de disponibilidade de portas"))
        self.btnconsultanalistas.setText(_translate("MainWindow", "Consulta de contato On Call Duty Analistas"))
        self.btninformacoes.setText(_translate("MainWindow", "Informações para abertura de chamado"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btncalc.setText(_translate("MainWindow", "Caculadora de IP"))
        self.btnlitc.setText(_translate("MainWindow", "Notificar Call UP LITC"))
        self.btnexterno.setText(_translate("MainWindow", "Call UP Vinhedo, CLE, LPC"))
        self.btnping.setText(_translate("MainWindow", "Ping"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
from servicos import servicosdoc_rc
