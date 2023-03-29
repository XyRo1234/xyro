import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.btnProperty.clicked.connect(self.showP_BasedMsg)
        self.btnButtonOverload.clicked.connect(self.addButton)
        self.btnCritical.clicked.connect(lambda:
                                         QMessageBox.critical(self, 'critical', 'critical message'))

        self.btnInfo.clicked.connect(lambda:
                                     QMessageBox.information(self, 'information', 'infomation message',
                                                             QMessageBox.Ok | QMessageBox.Cancel))
        self.btnQuestion.clicked.connect(lambda:
                                         QMessageBox.question(self, 'question', 'question message',
                                                              QMessageBox.Yes | QMessageBox.No))
        self.btnWarning.clicked.connect(lambda:
                                        QMessageBox.warning(self, 'warning', 'warning message',
                                                            QMessageBox.Retry | QMessageBox.Ignore))
        self.btnCritical_2.clicked.connect(self.showCirticalMsg)
        self.btnInfo_2.clicked.connect(self.showInfoMsg)
        self.btnQuestion_2.clicked.connect(self.showQuestionMsg)
        self.btnWarning_2.clicked.connect(self.showWarningMsg)

    def showCirticalMsg(self):
        # property-based API를 이용하여 작성
        msgbox = QMessageBox()
        msgbox.setWindowTitle("critical")
        msgbox.setText('critical message')
        msgbox.setIcon(QMessageBox.Critical)
        r = msgbox.exec()

    def showInfoMsg(self):
        # property-based API를 이용하여 작성
        msgbox = QMessageBox()
        msgbox.setWindowTitle("information")
        msgbox.setText('information message')
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        r = msgbox.exec()

    def showQuestionMsg(self):
        # property-based API를 이용하여 작성
        msgbox = QMessageBox()
        msgbox.setWindowTitle("warning")
        msgbox.setText('warning message')
        msgbox.setIcon(QMessageBox.Question)
        msgbox.setStandardButtons(QMessageBox.Retry | QMessageBox.Ignore)
        r = msgbox.exec()

    def showWarningMsg(self):
        # property-based API를 이용하여 작성
        msgbox = QMessageBox()
        msgbox.setWindowTitle("question")
        msgbox.setText('question message')
        msgbox.setIcon(QMessageBox.Question)
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        r = msgbox.exec()

    def showP_BasedMsg(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("WindowTitle: 타이틀")
        msgbox.setText('Text: 간단한 메시지 입니다')
        msgbox.setInformativeText("InformativeText: 추가 정보제공 메시지")
        msgbox.setStandardButtons(QMessageBox.Discard | QMessageBox.Cancel | QMessageBox.Save)
        msgbox.setDefaultButton(QMessageBox.Save)
        msgbox.setDetailedText('DetailedText\n자세한 정보는 이곳에 출력 가능')
        # msgbox.setIconPixmap(QPixmap('google.png'))
        msgbox.setIcon(QMessageBox.Critical)
        r = msgbox.exec()
        if r == QMessageBox.Save:
            print("save")
        elif r == QMessageBox.Cancel:
            print("Cancel")
        elif r == QMessageBox.Discard:
            print("Discard")
        else:
            print("Invalid")

    def addButton(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("사용자 버튼 만들기")
        msgbox.setText("사용자 버튼 만드는 법")
        msgbox.setIcon(QMessageBox.Information)
        ok = msgbox.addButton('User OK', QMessageBox.AcceptRole)
        cancel = msgbox.addButton('User Cancel', QMessageBox.RejectRole)
        abort = msgbox.addButton(QMessageBox.Abort)

        r = msgbox.exec()
        print('msgbox.exec :', r)
        r = msgbox.clickedButton()
        print('clickedButton:', r)
        if r == ok:
            print("Press User OK")
        elif r == cancel:
            print("Press User Cancel")
        elif r == abort:
            print("Press Abort")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
