import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow

class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.tick = 0
        self.mode = 1
        self.rstatus = False
        self.gstatus = False
        self.setupUi(self)
        self.timer = QTimer()
        self.btnCase1.clicked.connect(lambda: self.startTimer(1))
        self.btnCase2.clicked.connect(lambda: self.startTimer(2))
        self.timer.timeout.connect(lambda: self.displayLed(self.mode))
        self.led_control()

    def displayLed(self, mode):
        self.tick = self.tick + 1

        if self.tick % mode == 0: self.rstatus = not self.rstatus
        if self.tick % (mode + 1) == 0: self.gstatus = not self.gstatus
        self.led_control(red=self.rstatus, green=self.gstatus)

    def led_control(self, red=False, green=False):
        if red == 0:
            self.lblRed.setStyleSheet("background-color: black;")
        elif red == 1:
            self.lblRed.setStyleSheet("background-color: red;")
        if green == 0:
            self.lblGreen.setStyleSheet("background-color: black;")
        elif green == 1:
            self.lblGreen.setStyleSheet("background-color: green;")

    def startTimer(self, mode):
        self.tick = 0
        self.led_control()
        self.mode = mode
        self.timer.start(500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
