import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.combo_method)

        self.cboActivate.activated.connect(self.activate)
        self.cboHighlight.highlighted.connect(self.highlighted)

        self.cboNoEdit.currentIndexChanged['QString'].connect(self.index_changed)
        self.cboNoEdit.currentTextChanged.connect(self.text_changed)
        self.cboNoEdit.editTextChanged.connect(self.editTextChanged)

        self.cboEdit.currentIndexChanged['QString'].connect(self.index_changed)
        self.cboEdit.currentTextChanged.connect(self.text_changed)
        self.cboEdit.editTextChanged.connect(self.editTextChanged)

    def combo_method(self):
        print('총갯수:', self.cboEdit.count())
        print('현재 선택된 index:', self.cboEdit.currentIndex())
        print('현재 선택된 text:', self.cboEdit.currentText())

    def activate(self, index):
        print('activate', index)

    def index_changed(self, index):
        print('index_changed', index)

    def highlighted(self, index):
        print('highlighted', index)

    def text_changed(self, index):
        print('text_changed', index)

    def editTextChanged(self, index):
        print('editTextChanged', index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
