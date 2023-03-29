import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime, QTime

GUI_FILE_NAME = 'gui_sol'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui_sol import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.DateTimeEdit.dateChanged.connect(self.dateChage)
        self.btnToday.clicked.connect(self.setToday)

        self.DateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def dateChage(self, date):
        self.lblMsg.setText('선택한 날짜는 {} 입니다'.format(date.toString('yyyy년 MM월 dd일')))

    def setToday(self):
        self.DateTimeEdit.setDateTime(QDateTime.currentDateTime())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()

    sys.exit(app.exec_())
