from TestTranslator import Ui_MainWindow
 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
import sys
 
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
 
        #  翻译家
        self.trans = QTranslator()
      
        # 连接到槽函数
        self.BtnEn.clicked.connect(self._trigger_english)
        self.BtnCh.clicked.connect(self._trigger_zh_cn)
 
    def _trigger_english(self):
        print("[MainWindow] Change to English")
        self.trans.load(".\en")
        _app = QApplication.instance()  # 获取app实例
        _app.installTranslator(self.trans)
        # 重新翻译界面
        self.retranslateUi(self)
        print("End")
        pass
 
    def _trigger_zh_cn(self):
        print("[MainWindow] Change to zh_CN")
        self.trans.load("zh_CN")
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)
        pass
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow._trigger_english()
    mainWindow.show()
    sys.exit(app.exec_())