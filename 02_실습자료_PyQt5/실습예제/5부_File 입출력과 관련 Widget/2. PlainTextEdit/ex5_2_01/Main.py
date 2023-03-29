import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.setupUi(self)

        self.chkWrap.toggled.connect(self.txtEditor1.setLineWrapMode)
        self.btnLoad.clicked.connect(self.load_file)
        self.btnAppend.clicked.connect(self.append_text)
        self.btnMax.clicked.connect(self.set_maxblock)
        self.btnIns.clicked.connect(self.set_insmode)
        self.btnGroupWarp.buttonClicked.connect(self.set_word_wrap)

    def load_file(self):
        with open('Main.py', 'rt', encoding='utf-8') as f:
            s = f.read()
            self.txtEditor1.setPlainText(s)
            self.txtEditor2.setPlainText(s)

    def append_text(self):
        stxt = 'append: %d' % self.cnt
        self.txtEditor1.appendPlainText(stxt)
        self.txtEditor2.appendPlainText(stxt)
        self.cnt = self.cnt + 1

    def set_maxblock(self):
        max_block = int(self.editMax.text())
        self.txtEditor1.setMaximumBlockCount(max_block)
        self.txtEditor2.setMaximumBlockCount(max_block)

    def set_insmode(self, overwrite):
        self.txtEditor1.setOverwriteMode(overwrite)
        self.txtEditor2.setOverwriteMode(overwrite)
        self.btnIns.setText('수정모드' if overwrite else '삽입모드')

    def set_word_wrap(self, rdobtn):
        d = {'NoWrap': QTextOption.NoWrap, 'WordWrap': QTextOption.WordWrap,
             'WrapAnywhere': QTextOption.WrapAnywhere,
             'WrapAtWordBoundaryOrAnywhere': QTextOption.WrapAtWordBoundaryOrAnywhere}
        self.txtEditor1.setWordWrapMode(d[rdobtn.text()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    app.installEventFilter(w)
    w.show()
    sys.exit(app.exec_())
