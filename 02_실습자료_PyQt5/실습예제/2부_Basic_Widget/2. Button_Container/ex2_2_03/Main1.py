import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.lang = ''
        self.setupUi(self)

        self.lblMsg.setText('나는 사용할 수 있는 언어가 없다')

        self.chkTri.stateChanged.connect(self.chkTri_stateChanged)
        self.chkTri.toggled.connect(self.chkTri_toggled)

        self.chkC.toggled.connect(self.Use_Lang)
        self.chkCpp.toggled.connect(self.Use_Lang)
        self.chkJava.toggled.connect(self.Use_Lang)
        self.chkPython.toggled.connect(self.Use_Lang)

    def chkTri_stateChanged(self, arg):
        print('state changed', arg)
        print('checkState()', self.chkTri.checkState())
        print('isChecked()', self.chkTri.isChecked())
        print()

    def chkTri_toggled(self, arg):
        print('toggled', arg)

    def Use_Lang(self):
        l = []
        if self.chkC.isChecked(): l.append('C')
        if self.chkCpp.isChecked(): l.append('C++')
        if self.chkJava.isChecked(): l.append('Java')
        if self.chkPython.isChecked(): l.append('Python')
        if l:
            print(f"나는 {','.join(l)}언어를 사용할 수 있다.")
        else: print(f'나는 사용할 수 있는 언어가 없다')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
