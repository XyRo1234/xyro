import sys,os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o '+GUI_FILE_NAME+'.py')
from gui import Ui_MainWindow


class Form(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.year = '1학년'
        self.gender = '남자'
        self.setupUi(self)

        self.btnOK.clicked.connect(self.btnOK_Click)
        self.buttonGroup_grade.buttonClicked.connect(self.func2)
        self.buttonGroup_sex.buttonClicked.connect(self.func)
        
        # Todo : radio 버튼의 시그널 슬롯 연결

    def func(self, btn):
        self.gender = btn.text()

    def func2(self, btn):
        self.year = btn.text()

    def btnOK_Click(self):
        # radio1, radio2, radio3
        # buttonGroup_grade, buttonGroup_sex
        
        self.lblMsg.setText('{} {} 입니다.'.format(self.year, self.gender))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())



