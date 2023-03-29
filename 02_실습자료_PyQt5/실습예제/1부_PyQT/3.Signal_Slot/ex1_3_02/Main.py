import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 시그널/슬롯 연결
        self.btnHello.clicked.connect(self.print_hello)
        self.btnWorld.clicked.connect(self.print_world)

    def print_hello(self):
        self.lblMsg.setText("Hello")

    def print_world(self):
        self.lblMsg.setText("World")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
