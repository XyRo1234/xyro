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
        self.file = ''
        self.setupUi(self)
        self.btnNew.clicked.connect(self.new_file)
        self.btnAdd.clicked.connect(self.add_file)
        self.btnRead.clicked.connect(self.read_file)

    def new_file(self):
        self.file, _ = QFileDialog.getSaveFileName(self, '새 문서', filter='텍스트파일(*.txt)')
        if self.file:
            with open(self.file, 'wt') as f:
                pass
            self.setWindowTitle(QFileInfo(self.file).fileName())
            self.btnAdd.setEnabled(True)

    def add_file(self):
        with open(self.file, 'at') as f:
            f.write(self.lineEdit.text() + '\n')

    def read_file(self):
        self.file, _ = QFileDialog.getOpenFileName(self, '열기', filter='텍스트파일(*.txt)')
        if self.file:
            with open(self.file, 'rt') as f:
                print(f.read())
            self.setWindowTitle(QFileInfo(self.file).fileName())
            self.btnAdd.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
