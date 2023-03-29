import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.idpass = {'AXQ1000': '123456', 'AXQ1001': '123456', 'AXQ1002': '123456', 'AXQ1003': '123456','AXQ1004': '123456'}
        self.btnOK.clicked.connect(self.Confirm_Password)
        self.btnChange.clicked.connect(self.Change)
        # self.linID.QRegExpValidator

    def ID_Check(self):
        for wid in self.findChildren(QLineEdit):    # self.linID  self.linPass
            if not wid.hasAcceptableInput():
                print(f'{self.formLayout.labelForField(wid).text()}를 입력해 주세요')
                return False
        return True
    
    def Confirm_Password(self):
        if not self.ID_Check():
            return
        if self.linID.text() not in self.idpass:
            print('없는 아이디 입니다')
            self.lblMsg.setText('없는 아이디 입니다')

        elif self.linPass.text() != self.idpass[self.linID.text()]:
            print('비밀번호가 틀렸습니다')
            self.lblMsg.setText('비밀번호가 틀렸습니다')
        else:
            print('인증되었습니다')
            self.lblMsg.setText('인증되었습니다')

    def Change(self):
        if not self.ID_Check():
            return
        if self.linID.text() not in self.idpass:
            self.lblMsg.setText('없는 아이디 입니다')
        else:
            self.idpass[self.linID.text()] = self.linPass.text()
            self.lblMsg.setText('비밀번호 변경 : [{}]'.format(self.linPass.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
