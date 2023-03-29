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
        self.cboSpecies.addItems(list(self.gb.groups.keys()))

        self.btnViolin.clicked.connect(self.drawViolinPlot)
        self.btnViolinDeco.clicked.connect(self.drawViolinDeco)
        self.cboSpecies.activated.connect(self.drawSpecies)

    def drawSpecies(self, index):
        item = self.df.columns.tolist()[0:-1]
        species = self.cboSpecies.itemText(index)
        l = [self.gb[x].get_group(species).tolist() for x in item]

        fig = plt.figure()
        plt.title(species)
        plt.violinplot(l, vert=False, showmedians=True, showmeans=True)
        plt.show()

    def drawViolinPlot(self):
        item = self.df.columns.tolist()[0:-1]
        l = [self.df[x].tolist() for x in item]
        plt.title('All Species')
        grp = plt.violinplot(l, positions=[2, 4, 6, 8], widths=[1, 2, 1, 0.5])
        plt.show()

    def drawViolinDeco(self):
        violin = plt.violinplot(self.df['petal_length'].tolist(),
                                showmeans=True,
                                showmedians=True,
                                quantiles=[[0.25, 0.75]])

        violin['cbars'].set_edgecolor('black')
        violin['cmaxes'].set_edgecolor('blue')
        violin['cmins'].set_edgecolor('purple')
        violin['cmeans'].set_edgecolor('magenta')
        violin['cmedians'].set_edgecolor('cyan')
        violin['cquantiles'].set_edgecolor('orange')
        violin['bodies'][0].set_facecolor('olive')
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
