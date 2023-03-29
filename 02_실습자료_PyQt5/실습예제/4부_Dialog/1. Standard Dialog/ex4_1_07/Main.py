import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui import Ui_MainWindow
from PyQt5.QtCore import Qt


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnDownLoadModal.clicked.connect(self.downloadModal)

    def downloadModal(self):
        minval, maxval = int(self.editMin.text()), int(self.editMax.text())

        progress = QProgressDialog('다운로드 중...', '취소', 0, 100)
        progress.canceled.connect(self.downAbort)
        progress.setWindowTitle('다운로드')
        progress.setWindowModality(Qt.ApplicationModal)
        progress.setMinimumDuration(int(self.editMinDuration.text()))
        progress.setRange(minval, maxval)
        progress.setValue(0)
        for i in range(minval + 1, maxval + 1):
            print('work', i)
            progress.setValue(i)
            if progress.wasCanceled():
                print('canceled')
                return
        print("Finish")

    def downAbort(self):
        print('abort')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
