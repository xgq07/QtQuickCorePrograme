# -*- coding: utf-8 -*-
from PyQt5.QtCore import QUrl,QTranslator
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine
import sys
if __name__ == '__main__':
    path = 'main.qml'   # 加载的QML文件
    try:
        app = QGuiApplication([])
        engine = QQmlApplicationEngine() 
        trans = QTranslator()
        trans.load("zh_CN")
        app.installTranslator(trans)
        print(1111111111111)
        engine.retranslate()
        engine.load(QUrl(path))
        app.exec()
    except Exception as e:
        print(e)

    sys.exit()
   