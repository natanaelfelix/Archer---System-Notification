# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_inter.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 20, 431, 31))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 50, 491, 41))
        self.label_4.setObjectName("label_4")
        self.btnsair = QtWidgets.QPushButton(self.centralwidget)
        self.btnsair.setGeometry(QtCore.QRect(700, 500, 93, 28))
        self.btnsair.setObjectName("btnsair")
        self.btnvoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnvoltar.setGeometry(QtCore.QRect(60, 500, 93, 28))
        self.btnvoltar.setObjectName("btnvoltar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 150, 541, 16))
        self.label_3.setObjectName("label_3")
        self.vivo = QtWidgets.QRadioButton(self.centralwidget)
        self.vivo.setGeometry(QtCore.QRect(60, 250, 141, 21))
        self.vivo.setObjectName("vivo")
        self.embratel = QtWidgets.QRadioButton(self.centralwidget)
        self.embratel.setGeometry(QtCore.QRect(60, 280, 141, 21))
        self.embratel.setObjectName("embratel")
        self.btnconsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnconsultar.setGeometry(QtCore.QRect(60, 320, 93, 28))
        self.btnconsultar.setObjectName("btnconsultar")
        self.resultadoconsulta = QtWidgets.QTextBrowser(self.centralwidget)
        self.resultadoconsulta.setGeometry(QtCore.QRect(210, 180, 581, 251))
        self.resultadoconsulta.setObjectName("resultadoconsulta")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 460, 181, 61))
        self.label_2.setStyleSheet("image: url(:/infodoc/scania-logo-2.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 171, 131))
        self.label_5.setStyleSheet("image: url(:/infodoc/information-160885_960_720.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archer 1.0 - Informações"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Archer -Sistema de notificações urgentes</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Informações para abertura de chamado</span></p></body></html>"))
        self.btnsair.setText(_translate("MainWindow", "Sair"))
        self.btnvoltar.setText(_translate("MainWindow", "Voltar"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Caso não encontre as informações necessárias entre em contato com o time de redes LITC</p></body></html>"))
        self.vivo.setText(_translate("MainWindow", "Operadora Vivo"))
        self.embratel.setText(_translate("MainWindow", "Operadora Embratel"))
        self.btnconsultar.setText(_translate("MainWindow", "Consultar"))
from informacoes import infodoc_rc