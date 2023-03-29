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
        self.btnBoxAll.clicked.connect(self.drawBoxPlot)
        self.cboSpecies.activated.connect(self.drawSpecies)

        self.gb = self.df.groupby('species')
        self.cboSpecies.addItems(list(self.gb.groups.keys()))

    def drawSpecies(self, index):
        item = self.df.columns.tolist()[0:-1]
        species = self.cboSpecies.itemText(index)
        l = [self.gb[x].get_group(species).tolist() for x in item]

        fig = plt.figure()
        plt.title(species)
        plt.boxplot(l, labels=item)
        plt.show()

    def drawBoxPlot(self):
        item = self.df.columns.tolist()[0:-1]
        l = [self.df[x].tolist() for x in item]
        plt.title('All Species')
        r = plt.boxplot(l, labels=item, notch=True, sym='b+')

        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
