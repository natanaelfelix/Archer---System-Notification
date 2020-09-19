# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status_inter.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 20, 431, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 580, 171, 71))
        self.label_2.setStyleSheet("image: url(:/statusdoc/scania-logo-2.png);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 50, 491, 41))
        self.label_4.setObjectName("label_4")
        self.btnsair = QtWidgets.QPushButton(self.centralwidget)
        self.btnsair.setGeometry(QtCore.QRect(610, 620, 93, 28))
        self.btnsair.setObjectName("btnsair")
        self.btnenviar = QtWidgets.QPushButton(self.centralwidget)
        self.btnenviar.setGeometry(QtCore.QRect(390, 530, 93, 28))
        self.btnenviar.setObjectName("btnenviar")
        self.btnvoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnvoltar.setGeometry(QtCore.QRect(160, 620, 93, 28))
        self.btnvoltar.setObjectName("btnvoltar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 100, 521, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 460, 471, 61))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 200, 221, 181))
        self.label_6.setStyleSheet("image: url(:/statusdoc/user_icon-6777e4b561110b37b511aed860a24e71.png);")
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 130, 258, 327))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputdestinatario = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputdestinatario.setObjectName("inputdestinatario")
        self.verticalLayout_2.addWidget(self.inputdestinatario)
        self.inputcopia = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputcopia.setObjectName("inputcopia")
        self.verticalLayout_2.addWidget(self.inputcopia)
        self.inputim = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputim.setObjectName("inputim")
        self.verticalLayout_2.addWidget(self.inputim)
        self.inputoperadorfp = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputoperadorfp.setObjectName("inputoperadorfp")
        self.verticalLayout_2.addWidget(self.inputoperadorfp)
        self.inputanalistslocal = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputanalistslocal.setObjectName("inputanalistslocal")
        self.verticalLayout_2.addWidget(self.inputanalistslocal)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.inputprotocolo = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputprotocolo.setObjectName("inputprotocolo")
        self.gridLayout.addWidget(self.inputprotocolo, 2, 0, 1, 1)
        self.inputoperadoralink = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputoperadoralink.setText("")
        self.inputoperadoralink.setObjectName("inputoperadoralink")
        self.gridLayout.addWidget(self.inputoperadoralink, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.inputobservcoes = QtWidgets.QTextEdit(self.layoutWidget)
        self.inputobservcoes.setObjectName("inputobservcoes")
        self.verticalLayout.addWidget(self.inputobservcoes)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archer 1.0 - Consulta de status dos chamados"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Archer -Sistema de notificações urgentes</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Consultar status de chamado com análistas</span></p></body></html>"))
        self.btnsair.setText(_translate("MainWindow", "Sair"))
        self.btnenviar.setText(_translate("MainWindow", "Enviar"))
        self.btnvoltar.setText(_translate("MainWindow", "Voltar"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">Preencha os campos para consultar os status dos chamaods com os analistas locais</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">Será eviado uma notificações para os times de network Brasil,</span></p><p align=\"center\"><span style=\" font-size:7pt;\">é de responsábilidade do operador de focal point a atualização sobre o caso.</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.inputdestinatario.setPlaceholderText(_translate("MainWindow", "Destinatário:"))
        self.inputcopia.setPlaceholderText(_translate("MainWindow", "Cópia:"))
        self.inputim.setPlaceholderText(_translate("MainWindow", "Numero de IM:"))
        self.inputoperadorfp.setPlaceholderText(_translate("MainWindow", "Operador do focal point:"))
        self.inputanalistslocal.setPlaceholderText(_translate("MainWindow", "Análista local:"))
        self.inputprotocolo.setPlaceholderText(_translate("MainWindow", "Protocolo:"))
        self.inputoperadoralink.setPlaceholderText(_translate("MainWindow", "Operadora do Link:"))
        self.inputobservcoes.setPlaceholderText(_translate("MainWindow", "Observações:"))
from decisao.status import statusdoc_rc