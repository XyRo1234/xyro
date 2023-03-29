import sys, os

from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import pandas as pd

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


# 한글 지원
# import matplotlib
# import matplotlib.font_manager as fm
# fm.get_fontconfig_fonts()
# font_location = 'C:/Windows/Fonts/gulim.ttc' # For Windows
# font_name = fm.FontProperties(fname=font_location).get_name()
# matplotlib.rc('font', family=font_name)

class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.df = pd.read_csv('../IRIS.csv')
        self.gb = self.df.groupby('species')

        self.cboColumn.addItems(self.df.columns.tolist()[0:-1])
        self.btnHist.clicked.connect(self.drawHist)

    def drawHist(self):
        species = list(self.gb.groups.keys())
        item = self.cboColumn.currentText()

        l = [self.gb[item].get_group(x).tolist() for x in species]
        bins = 10 if self.lineEdit.text() == '' else int(self.lineEdit.text())
        r = plt.hist(l, label=species,
                     bins=bins,
                     histtype=self.cboHittype.currentText())
        plt.title('iris {} histogram'.format(item))
        plt.legend()
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
