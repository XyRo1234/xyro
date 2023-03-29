import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dialR.valueChanged.connect(self.func)
        self.dialG.valueChanged.connect(self.func)
        self.dialB.valueChanged.connect(self.func)

    def func(self):
        color_val = [self.dialR.value(), self.dialG.value(), self.dialB.value()]
        # print(color_val)
        # print(','.join(list(map(str,color_val))))
        # print(self.dialR.value() ^ 255,self.dialG.value() ^ 255,self.dialB.value() ^ 255)
        back_color = f"rgb({self.dialR.value()},{self.dialG.value()},{self.dialB.value()})"
        fore_color = f"rgb({self.dialR.value() ^ 255},{self.dialG.value() ^ 255},{self.dialB.value() ^ 255})"
        self.lblColor.setText(f'rgb({self.dialR.value()},{self.dialG.value()},{self.dialB.value()})')
        self.lblColor.setStyleSheet(f'background-color:{back_color}; color:{fore_color}' )
        # self.lblColor.setStyleSheet('background-color: {};color: {}'.format(back_color, fore_color))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
