import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnOK.clicked.connect(self.func)

    def func(self):
        if not self.LineEdit_4.hasAcceptableInput():
            self.lblError.setText('아이디 오류')
        elif not self.LineEdit_5.hasAcceptableInput():
            self.lblError.setText('전화번호오류')
        else:
            self.lblError.setText('모두 정상')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
