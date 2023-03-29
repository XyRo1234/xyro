import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'exam_gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from exam_gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setActionConnect()

    def setActionConnect(self):
        self.action_New.triggered.connect(self.newFile)
        # self.btnNew.clicked.connect(self.action_New.trigger)
        self.btnNew.clicked.connect(self.func)

    def func(self):
        self.action_New.trigger()

    def newFile(self):
        print('newFile')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
