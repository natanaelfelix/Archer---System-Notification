# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'disponibilidade_inter.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 652)
        MainWindow.setMinimumSize(QtCore.QSize(807, 652))
        MainWindow.setMaximumSize(QtCore.QSize(807, 652))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 431, 31))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 70, 301, 41))
        self.label_4.setObjectName("label_4")
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(140, 300, 541, 191))
        self.result.setObjectName("result")
        self.btnconsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnconsultar.setGeometry(QtCore.QRect(580, 250, 93, 28))
        self.btnconsultar.setObjectName("btnconsultar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 110, 151, 121))
        self.label_2.setStyleSheet("image: url(:/disponibilidadedoc/418414.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 520, 231, 81))
        self.label_3.setStyleSheet("image: url(:/disponibilidadedoc/scania-logo-2.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(140, 240, 371, 53))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnhost = QtWidgets.QLineEdit(self.widget)
        self.btnhost.setObjectName("btnhost")
        self.gridLayout.addWidget(self.btnhost, 0, 0, 1, 1)
        self.btnporta = QtWidgets.QLineEdit(self.widget)
        self.btnporta.setObjectName("btnporta")
        self.gridLayout.addWidget(self.btnporta, 1, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(60, 560, 691, 51))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnvoltar = QtWidgets.QPushButton(self.widget1)
        self.btnvoltar.setObjectName("btnvoltar")
        self.horizontalLayout.addWidget(self.btnvoltar, 0, QtCore.Qt.AlignLeft)
        self.btnsair = QtWidgets.QPushButton(self.widget1)
        self.btnsair.setObjectName("btnsair")
        self.horizontalLayout.addWidget(self.btnsair, 0, QtCore.Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archer 1.0 - Serviços"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Archer -Sistema de notificações urgentes</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Consulta de status de portas</span></p></body></html>"))
        self.btnconsultar.setText(_translate("MainWindow", "Consultar"))
        self.btnhost.setPlaceholderText(_translate("MainWindow", "Digite o hostname ou o numero de IP:"))
        self.btnporta.setPlaceholderText(_translate("MainWindow", "Digite a interface:"))
        self.btnvoltar.setText(_translate("MainWindow", "Voltar"))
        self.btnsair.setText(_translate("MainWindow", "Sair"))
from disponibilidade import disponibilidadedoc_rc
