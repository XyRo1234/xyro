import sys, os

from PyQt5.QtWidgets import *
from matplotlib import pyplot as plt

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnDraw.clicked.connect(self.drawGraph)
        loclist = ['upper left', 'upper right', 'lower left', 'lower right',
                   'upper center', 'lower center', 'center left', 'center right',
                   'center', 'best'
                   ]
        self.legendLocComboBox.addItems(loclist)

    def drawGraph(self):
        plt.plot(['Moon', 'Song', 'Lew'], [80, 70, 95], label='KOR')
        plt.plot(['Moon', 'Song', 'Lew'], [75, 100, 80], label='ENG')

        plt.title(self.titleLineEdit.text())
        plt.xlabel(self.xlabelLineEdit.text())
        plt.ylabel(self.ylabelLineEdit.text())
        loc = self.legendLocComboBox.currentText()
        if self.legendLineEdit.text():
            plt.legend(self.legendLineEdit.text().split(','), loc=loc)
        else:
            plt.legend(loc=loc)
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
