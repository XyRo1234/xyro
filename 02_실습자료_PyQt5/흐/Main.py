
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

GUI_FILE_NAME = 'gui'
DIALOG_FILE_NAME = 'dialog'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
os.system('python -m PyQt5.uic.pyuic -x ' + DIALOG_FILE_NAME + '.ui -o ' + DIALOG_FILE_NAME + '.py')
from gui import Ui_MainWindow
from dialog import Ui_Dialog


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.Open_Action)
        pixmap = QPixmap(':/image/image_iner.jpg')   # (':/image/image_iner.jpg')  (r'.\image_iner.jpg')
        self.lbl_image.setPixmap(pixmap)
        self.lbl_image.resize(pixmap.size())
        self.lblPage.setText('')
        self.btn_Left.clicked.connect(self.pagesetting_minus)
        self.btn_Right.clicked.connect(self.pagesetting_plus)
        self.btn_setting.clicked.connect(self.setting)
        self.btn_setting_2.clicked.connect(self.setting_2)
        self.pages = []
        self.page = 0
        self.pagelen = 0
        self.color_info = ''
        self.Open(r'./txt/인어공주.txt')

    def pagesetting_minus(self):
        if self.page==0: return
        self.page -= 1
        print(self.page)
        self.textEdit.setText(self.pages[self.page])
        self.lblPage.setText(f'{self.page+1}/{self.pagelen}')

    def pagesetting_plus(self):
        print(self.page, self.pagelen)
        if self.page==self.pagelen-1: return
        self.page += 1
        print(self.page)
        self.textEdit.setText(self.pages[self.page])
        self.lblPage.setText(f'{self.page+1}/{self.pagelen}')
    
    def Open_Action(self):
        show_filter = 'All(*.*)'
        filepath, filter_type = QFileDialog.getOpenFileName(directory=r'./txt/' ,filter=show_filter)
        self.Open(filepath)

    def Open(self, filepath):
        name = os.path.basename(filepath)
        name = name.split('.')[0]
        pixmap = QPixmap(f'./image/{name}.jpg')
        self.lbl_image.setPixmap(pixmap)
        self.lbl_image.resize(pixmap.size())
        cut_list = []
        self.pages = []
        with open(filepath, 'r', encoding='utf-8') as fl:
            lines = fl.readlines()
            for line in lines:
                while line:
                    cut_list.append(line[:56])
                    line = line[56:]        
        while cut_list:
            a = ''
            if len(cut_list)>=42: e=42
            else: e=len(cut_list)
            for i in range(0,e):
                # print(i,':' , cut_list[i])
                a = a + cut_list[i]
            self.pages.append(a)
            cut_list = cut_list[e:]
        self.pagelen = len(self.pages)
        self.textEdit.setText(self.pages[0])
        self.lblPage.setText(f'{self.page+1}/{self.pagelen}')
        self.setWindowTitle(name)


    def setting(self):
        font, r = QFontDialog.getFont()
        # font, r = QFontDialog.getFont( QFont("굴림",10, QFont.Bold, True))
        # font, r = QFontDialog.getFont(self.lineEdit.font())
        print(font.family(), font.pointSize(), r)
        if r: self.textEdit.setFont(font)

    def setting_2(self):
        dlg = dlgForm(self)
        dlg.open()



class dlgForm(QDialog, Ui_Dialog):

    def __init__(self, parent=None, flag=Qt.Dialog):
        super().__init__(parent, flag)
        self.setupUi(self)
        # Todo :  넘어온 name를 line edit에 표시
        self.btn_w.clicked.connect(self.white)
        self.btn_black.clicked.connect(self.black)
    def white(self):
        print('흰색')
        self.parent().textEdit.setStyleSheet('background-color: white; color: black;')

    def black(self):
        print('검은색')
        self.parent().textEdit.setStyleSheet('background-color: black; color: white;')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
