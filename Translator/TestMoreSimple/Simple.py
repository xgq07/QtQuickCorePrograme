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
    def __init__(self,trans,parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self._app = app
        self._trans = trans

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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(-130, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.btnCh = QtWidgets.QPushButton(self.centralwidget)
        self.btnCh.setGeometry(QtCore.QRect(130, 210, 75, 23))
        self.btnCh.setObjectName("btnCh")
        self.BtnEn = QtWidgets.QPushButton(self.centralwidget)
        self.BtnEn.setGeometry(QtCore.QRect(280, 210, 75, 23))
        self.BtnEn.setObjectName("BtnEn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 连接到槽函数
        self.BtnEn.clicked.connect(self._trigger_english)
        self.btnCh.clicked.connect(self._trigger_zh_cn)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _trigger_english(self):
        print("[MainWindow] Change to English")
        self._trans.load("en")
        _app = QApplication.instance()  # 获取app实例
        _app.installTranslator(self._trans)
        # 重新翻译界面
        self.retranslateUi(self)
        print("End")
        pass
 
    def _trigger_zh_cn(self):
        print("[MainWindow] Change to zh_CN")
        self._trans.load("zh_CN")
        _app = QApplication.instance()
        _app.installTranslator(self._trans)
        self.retranslateUi(self)
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnHello.setText(_translate("MainWindow", "Hello Man"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.btnCh.setText(_translate("MainWindow", "中文"))
        self.BtnEn.setText(_translate("MainWindow", "英文"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    trans = QtCore.QTranslator()
    #trans.load("zh_CN")
    app.installTranslator(trans)
    window = Ui_MainWindow(trans)
    window.show()
    sys.exit(app.exec_())
