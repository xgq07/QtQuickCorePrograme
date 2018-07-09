# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Simple.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
import sys

class Ui_MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnHello = QtWidgets.QPushButton(self.centralwidget)
        self.btnHello.setGeometry(QtCore.QRect(120, 40, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btnHello.setFont(font)
        self.btnHello.setObjectName("btnHello")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnHello.setText(_translate("MainWindow", "Hello Man"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    trans = QtCore.QTranslator()
    trans.load("en")
    app.installTranslator(trans)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
