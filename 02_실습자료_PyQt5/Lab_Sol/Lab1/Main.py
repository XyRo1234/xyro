import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lblState.setStyleSheet('background-color:red')
        self.cnt = 0
        self.btnPush.clicked.connect(self.change_color)
        self.btnToggle.toggled.connect(self.Toggle_Color)
    
    def change_color(self):
        self.cnt += 1
        if self.cnt%3==1:   self.lblColor.setStyleSheet('background-color:red')
        elif self.cnt%3==2: self.lblColor.setStyleSheet('background-color:green')
        else:               self.lblColor.setStyleSheet('background-color:blue')

    def Toggle_Color(self,a):
        if a:
            self.lblState.setStyleSheet('background-color:green')
            self.btnToggle.setText('ON')
        else:
            self.lblState.setStyleSheet('background-color:red')
            self.btnToggle.setText('OFF')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
