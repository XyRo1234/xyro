import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

MAIN_FILE_NAME = 'main_wnd'
DIALOG_FILE_NAME = 'dialog'
os.system('python -m PyQt5.uic.pyuic -x ' + MAIN_FILE_NAME + '.ui -o ' + MAIN_FILE_NAME + '.py')
os.system('python -m PyQt5.uic.pyuic -x ' + DIALOG_FILE_NAME + '.ui -o ' + DIALOG_FILE_NAME + '.py')
from main_wnd import Ui_MainWindow
from dialog import Ui_Dialog


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnFind.clicked.connect(self.showFindDialog)

    def showFindDialog(self):
        dlg = dlgForm(self)
        dlg.exec()


class dlgForm(QDialog, Ui_Dialog):

    def __init__(self, parent=None, flag=Qt.Dialog):
        super().__init__(parent, flag)
        self.setupUi(self)
        self.widOption.setVisible(False)
        self.btnMore = self.buttonBox.addButton('&More', QDialogButtonBox.ActionRole)
        self.btnMore.setCheckable(True)
        self.btnMore.toggled.connect(self.widOption.setVisible)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
