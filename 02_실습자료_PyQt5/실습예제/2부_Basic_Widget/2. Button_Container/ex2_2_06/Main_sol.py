import sys,os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui_sol'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o '+GUI_FILE_NAME+'.py')
from gui_sol import Ui_MainWindow


class Form(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.year = '1학년'
        self.gender = '남자'
        self.setupUi(self)

        self.grpYear.buttonClicked.connect(self.getYear)
        self.grpGender.buttonClicked.connect(self.getGender)
        self.btnOK.clicked.connect(self.btnOK_Click)

    def getYear(self, radio):
        self.year = radio.text()

    def getGender(self, radio):
        self.gender = radio.text()

    def btnOK_Click(self):
        self.lblMsg.setText('{} {} 입니다.'.format(self.year, self.gender))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())



