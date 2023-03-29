import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.memory = 0
        self.val = ''
        self.btnGroupDisp.buttonClicked.connect(self.func)
        self.btnGroupOp.buttonClicked.connect(self.Op)
        self.btnMC.clicked.connect(self.MC)
        self.btnMR.clicked.connect(self.MR)
        self.btnMS.clicked.connect(self.MS)
        self.btnMp.clicked.connect(self.Mp)
        self.btnMm.clicked.connect(self.Mm)
    # def Chk(self):
    #     if self.val.isnumeric:
    #         print('MC', self.val)
    #     else:
    #         print('error')

    def MC(self):
        self.memory = 0
        self.lblDisp2.setStyleSheet('')
        self.lblDisp2.setText('0')
        print('MC', self.memory)

    def MR(self):
        if self.lblDisp.text()[-1]=='+': result = self.lblDisp.text() +  str(self.memory)
        elif self.lblDisp.text()[-1]=='/': result = self.lblDisp.text() +  str(self.memory)
        elif self.lblDisp.text()[-1]=='-': result = self.lblDisp.text() +  str(self.memory)
        elif self.lblDisp.text()[-1]=='*': result = self.lblDisp.text() +  str(self.memory)
        else: result = str(self.memory)

        self.lblDisp.setText(str(result))
        self.val = str(result)
        print('MR', self.memory)

    def MS(self):
        if not self.lblDisp.text().isnumeric(): return
        self.memory = int(self.lblDisp.text())
        self.lblDisp2.setText(str(self.memory))
        self.lblDisp2.setStyleSheet('background-color: red')
        self.val = ''
        self.lblDisp.setText('0')
        print('MS', self.memory)

    def Mp(self):
        # self.lblDisp.text()   # str
        if not self.lblDisp.text().isnumeric(): return
        self.memory = self.memory + int(self.lblDisp.text())
        self.val = ''
        self.lblDisp2.setText(str(self.memory))
        self.lblDisp.setText('0')
        self.lblDisp2.setStyleSheet('background-color: red')
        print('Mp', self.memory)

    def Mm(self):
        if not self.lblDisp.text().isnumeric(): return
        self.memory = self.memory - int(self.lblDisp.text())
        self.val = ''
        self.lblDisp2.setText(str(self.memory))
        self.lblDisp.setText('0')
        self.lblDisp2.setStyleSheet('background-color: red')
        print('Mm', self.memory)


    def func(self, btn):
        # print(btn.text())
        self.val = self.val + btn.text()
        self.lblDisp.setText(self.val)

    def Op(self, btn):
        if btn == self.btnC:
            self.val = ''
            self.lblDisp.setText('0')
        elif btn == self.btnBack:
            self.val = self.val[:-1]
            self.lblDisp.setText(self.val) if self.val else self.lblDisp.setText('0')
        elif btn == self.btnResult:
            if self.val=='': return
            try:
                result = eval(self.val)
                self.val = str(result)
            except:
                result = 'ERROR'
            print(result)
            self.lblDisp.setText(str(result))
            # self.val = ''

# lblDisp



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
