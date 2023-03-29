import sys, os
from PyQt5.QtWidgets import *

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
                txt = f'{self.formLayout.labelForField(wid).text()}를 입력해 주세요'
                QMessageBox.critical(self, 'a' , txt)
                return False
        return True
    
    def Confirm_Password(self):
        if not self.ID_Check():
            return
        if self.linID.text() not in self.idpass:
            print('없는 아이디 입니다')
            QMessageBox.warning(self, 'warning' , '없는 아이디 입니다')
        elif self.linPass.text() != self.idpass[self.linID.text()]:
            print('비밀번호가 틀렸습니다')
            QMessageBox.warning(self, 'warning' , '비밀번호가 틀렸습니다')
        else:
            print('인증되었습니다')
            QMessageBox.information(self, 'a' , '인증되었습니다')

    def Change(self):
        if not self.ID_Check():
            return
        if self.linID.text() not in self.idpass:
            QMessageBox.warning(self, 'warning' , '없는 아이디 입니다')
        else:
            r = QMessageBox.question(self, 'question', '비밀번호를 변경하시겠습니까?')
            print(r)
            if r == QMessageBox.Yes:
                self.idpass[self.linID.text()] = self.linPass.text()
                QMessageBox.information(self, 'information', f'비밀번호 변경: [{ self.idpass[self.linID.text()] }]')
            elif r== QMessageBox.No:
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
