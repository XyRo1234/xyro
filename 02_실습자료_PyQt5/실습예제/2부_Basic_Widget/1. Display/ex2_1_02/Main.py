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

        # Todo : label_3에 pixmap 클래스를 이용하여 그림추가
        pixmap = QPixmap(':/icon/images/setting.png')
        # pixmap = QPixmap(r'.\실습예제\2부_Basic_Widget\1. Display\images\setting.png')
        self.label_3.setPixmap(pixmap)
        self.label_3.resize(pixmap.size())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
