import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actionNew.triggered.connect(self.filenew)
        self.actionClose.triggered.connect(self.exit)
        self.actionBold.toggled.connect(lambda : self.bold(self.actionBold))


    def filenew(self):
        print('filenew')

    def exit(self):
        QApplication.exit()
    
    def bold(self, x):
        print('bold', x)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
