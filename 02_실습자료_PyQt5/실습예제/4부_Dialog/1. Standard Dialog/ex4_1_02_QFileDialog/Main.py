import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.btngetOpenFile.clicked.connect(self.getOpenFile)
        self.btngetSaveFile.clicked.connect(self.getSaveFile)
        self.btnExitDir.clicked.connect(self.getExistDir)
        self.btnExitDirUrl.clicked.connect(self.getExistDirUrl)

    def getOpenFile(self):
        show_filter = "모든 파일(*.*);;텍스트파일(*.txt);; 파이썬파일(*.py);; jpg(*.jpg;*.jpeg)"
        init_filter = "파이썬파일(*.py)"     # 최초 표시할 필터
        selected_file_name = "선택파일 없음"
        opt = QFileDialog.Option()
        # opt = QFileDialog.ShowDirsOnly | QFileDialog. DontUseNativeDialog
        filepath, filter_type = QFileDialog.getOpenFileName(filter=show_filter, initialFilter=init_filter, options=opt)
        print(filepath, filter_type)
        # self.lblOpenFileName.setText(filepath.split('/')[-1])
        self.lblOpenFileName.setText(os.path.basename(filepath))
        

        ''' 
        Todo
        OK를 누를 경우에만 다음동작 수행 
        1. 파일 이름.확장자를 self.lblOpenFileName에 표시하라
        2. 윈도우의 타이틀바 caption에 파일 이름.확장자를 표시하라
         
        '''

    def getSaveFile(self):
        show_filter = "모든 파일(*.*);;텍스트파일(*.txt);; 파이썬파일(*.py)"
        init_filter = "파이썬파일(*.py)"
        selected_file_name = "선택파일 없음"

        opt = QFileDialog.Option()
        # opt = QFileDialog.DontConfirmOverwrite

        filepath, filter_type = QFileDialog.getSaveFileName(filter=show_filter, initialFilter=init_filter, options=opt)
        print(filepath, filter_type)
        print(filepath.split('/')[-1])
        # self.lblSaveFileName.setText(filepath.split('/')[-1])
        self.lblSaveFileName.setText(os.path.basename(filepath))
        ''' 
        Todo
        OK를 누를 경우에만 다음동작 수행
        1. 파일 이름.확장자를 self.lblSaveFileName에 표시하라 
        '''

    def getExistDir(self):
        r = QFileDialog.getExistingDirectory(directory=self.linePath.text())
        self.linePath.setText(r)

    def getExistDirUrl(self):
        r = QFileDialog.getExistingDirectoryUrl(directory=QUrl(self.linePath.text()))
        print(r.toString())
        self.linePathUrl.setText(r.toString())
        url_link = '<a href="' + r.toString() + '">' + r.toString() + '</a>'
        self.label.setText(url_link)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
