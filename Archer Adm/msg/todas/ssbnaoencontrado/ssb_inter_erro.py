# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ssb_inter_erro.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(444, 368)
        MainWindow.setMinimumSize(QtCore.QSize(444, 368))
        MainWindow.setMaximumSize(QtCore.QSize(444, 368))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 241, 191))
        self.label.setStyleSheet("image: url(:/ssbnaoencontradodoc/unnamed.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 220, 291, 91))
        self.label_2.setObjectName("label_2")
        self.btnsair = QtWidgets.QPushButton(self.centralwidget)
        self.btnsair.setGeometry(QtCore.QRect(170, 320, 111, 28))
        self.btnsair.setObjectName("btnsair")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mensagem"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Não foi possivel localizar,</span></p><p align=\"center\"><span style=\" font-weight:600;\">verifique a informação digitada, </span></p><p align=\"center\"><span style=\" font-weight:600;\">e tente novamente...</span></p></body></html>"))
        self.btnsair.setText(_translate("MainWindow", "Sair"))

import msg.todas.ssbnaoencontrado.ssbnaoencontradodoc_rc