import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btngetFont.clicked.connect(self.getFont)

    def getFont(self):
        font, r = QFontDialog.getFont()
        # font, r = QFontDialog.getFont( QFont("굴림",10, QFont.Bold, True))
        # font, r = QFontDialog.getFont(self.lineEdit.font())
        print(font.family(), font.pointSize(), r)
        self.lineEdit.setFont(font)

        # self.lineEdit.setFont(QFontDialog.getFont(self.lineEdit.font())[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
