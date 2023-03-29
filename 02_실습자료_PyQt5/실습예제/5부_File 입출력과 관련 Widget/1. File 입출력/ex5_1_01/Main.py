import sys, os
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *


GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.file = ''
        self.setupUi(self)
        self.btnNew.clicked.connect(self.new_file)
        self.btnAdd.clicked.connect(self.line_add)
        self.btnRead.clicked.connect(self.read_file)

    
    def new_file(self):
        self.file, _ = QFileDialog.getSaveFileName(self,'새문서', filter='텍스트파일(*.txt)')
        if not self.file: return
        with open(self.file, 'w') as f:
            pass
        self.btnAdd.setEnabled(True)
    
    def line_add(self):
        with open(self.file, 'a') as f:
            f.write(self.lineEdit.text() + '\n')
            print('작성: ',self.lineEdit.text())
    
    
    def read_file(self):
        self.file, _ = QFileDialog.getOpenFileName(self, '열기', filter='텍스트파일(*.txt)')
        if not self.file: return
        name = os.path.basename(self.file)
        self.setWindowTitle(name)
        with open(self.file, 'r') as f:
            print('====읽어오기====')
            for l in f.readlines():
                print(l)
            print('====== 끝 ======')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
