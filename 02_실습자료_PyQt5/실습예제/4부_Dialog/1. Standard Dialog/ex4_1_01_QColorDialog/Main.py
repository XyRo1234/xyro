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
        self.dlgColor = QColorDialog()
        self.btnOption.clicked.connect(self.btnOption_Click)
        self.btnOpen.clicked.connect(self.btnOpen_Click)
        self.btnGetColor.clicked.connect(self.btnGetColor_Click)

        self.checkBox.toggled.connect(lambda x: self.dlgColor.setOption(QColorDialog.ShowAlphaChannel, on=x))
        self.checkBox_2.toggled.connect(lambda x: self.dlgColor.setOption(QColorDialog.NoButtons, on=x))
        self.checkBox_3.toggled.connect(lambda x: self.dlgColor.setOption(QColorDialog.DontUseNativeDialog, on=x))

        self.dlgColor.colorSelected.connect(self.selectColor)
        self.dlgColor.currentColorChanged.connect(self.changeColor)

    def btnOpen_Click(self, a):
        self.dlgColor.open(self.selectColor)

    def changeColor(self, color):
        self.lblChange.setStyleSheet("background-color : {}".format(color.name()))

    def selectColor(self):
        self.lblSelect.setStyleSheet("background-color : {}".format(self.dlgColor.selectedColor().name()))

    def btnOption_Click(self):
        color = self.dlgColor.getColor(Qt.red, options=self.dlgColor.options())
        if color.isValid():
            self.lblSelect.setStyleSheet("background-color : {}".format(color.name()))

    def btnGetColor_Click(self):
        options = QColorDialog.ColorDialogOptions()
        if self.checkBox.isChecked():
            options |= QColorDialog.ShowAlphaChannel
        elif self.checkBox_2.isChecked():
            options |= QColorDialog.NoButtons
        elif self.checkBox_3.isChecked():
            options |= QColorDialog.DontUseNativeDialog
        color = QColorDialog.getColor(options=options)  # 이것만 있으면 됨! # 표준다이얼로그

        if color.isValid():
            self.lblSelect.setStyleSheet("background-color : {}".format(color.name()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
