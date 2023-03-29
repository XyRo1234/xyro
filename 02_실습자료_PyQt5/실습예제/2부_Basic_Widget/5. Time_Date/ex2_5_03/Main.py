import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tmr = QTimer(self)
        # self.tmr.timeout.connect(lambda : self.timer(1))
        
        self.tick = 0
        self.btnCase1.clicked.connect(lambda : self.timer(1))
        self.btnCase2.clicked.connect(lambda : self.timer(2))
        

    # lblRed  lblGreen  btnCase1 btnCase2
    def timer(self, case):
        self.tick = 0
        if case==1:
            # self.tmr.stop()
            self.tmr.timeout.connect(self.case1)    # 여기가 문제
            self.tmr.start(500)
            # Form.case1(self)
        elif case==2:
            # self.tmr.stop()
            self.tmr.timeout.connect(self.case2)
            self.tmr.start(500)
            # Form.case2(self)

    def case1(self):
        self.tick +=1
        print('tick:', self.tick)
        if self.tick%2==0:
            self.lblRed.setStyleSheet("background-color: red; color:black;")
        elif self.tick%2==1:
            self.lblRed.setStyleSheet("background-color: black; color:red")
        # print(self.tick ,self.tick%4)
        if self.tick%4==0:
            self.lblGreen.setStyleSheet("background-color: black; color:green")
        elif self.tick%4==2:
            self.lblGreen.setStyleSheet("background-color: green; color:black")

    def case2(self):
        self.tick +=1
        print('tick:', self.tick)
        if self.tick%4==0:
            self.lblRed.setStyleSheet("background-color: red; color:black;")
        elif self.tick%4==2:
            self.lblRed.setStyleSheet("background-color: black; color:red")
        # print(self.tick ,self.tick%4)
        if self.tick%6==0:
            self.lblGreen.setStyleSheet("background-color: black; color:green")
        elif self.tick%6==3:
            self.lblGreen.setStyleSheet("background-color: green; color:black")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    # app.installEventFilter(w)
    w.show()
    sys.exit(app.exec_())
