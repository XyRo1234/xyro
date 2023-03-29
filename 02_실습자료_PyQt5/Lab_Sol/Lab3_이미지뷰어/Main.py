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

        self.btnOpen.clicked.connect(self.fileopen)

    def fileopen(self):
        directory = r'D:\01_SW_Reskilling\02.실습자료_배포용(V121)\실습예제\images'
        filter = "모든파일(*.*);;비트맵파일(*.bmp);;JPEG(*.jpg;*jpeg);;GIF(*.gif);;PNG(*.png);;ICO(*.ICO)"
        filepathname, fltr = QFileDialog.getOpenFileName(self, directory=directory, filter=filter)
        print(filepathname, fltr)
        name = os.path.basename(filepathname)
        pixmap = QPixmap(filepathname)
        self.lblImage.setPixmap(pixmap)
        self.lblImage.resize(pixmap.size())
        self.setWindowTitle(f'이미지뷰어: {name}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
