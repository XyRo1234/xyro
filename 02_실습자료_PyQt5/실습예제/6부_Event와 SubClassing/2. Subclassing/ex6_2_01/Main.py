import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow   # 여기 gui.py 안에서 myButton이 import되어있음


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.getCount)
        self.pushButton.clicked.connect(self.func)

    def func(self):
        print('clicked')

    def getCount(self):
        print(self.pushButton.getCount())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
