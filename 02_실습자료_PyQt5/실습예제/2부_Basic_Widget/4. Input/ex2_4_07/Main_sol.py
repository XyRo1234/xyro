import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui_sol'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui_sol import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dialR.valueChanged.connect(self.setColor)
        self.dialG.valueChanged.connect(self.setColor)
        self.dialB.valueChanged.connect(self.setColor)

    def setColor(self):
        back_color = "rgb({}, {}, {});".format(self.dialR.value(), self.dialG.value(), self.dialB.value())
        fore_color = "rgb({}, {}, {});".format(self.dialR.value() ^ 255, self.dialG.value() ^ 255,
                                               self.dialB.value() ^ 255)
        self.lblColor.setStyleSheet('background-color: {};color: {}'.format(back_color, fore_color))
        self.lblColor.setText(back_color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
