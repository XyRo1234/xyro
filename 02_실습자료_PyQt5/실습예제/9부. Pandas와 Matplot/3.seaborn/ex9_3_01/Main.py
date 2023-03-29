import sys, os

from PyQt5.QtWidgets import *
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

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
        self.btnScatter.clicked.connect(self.drawScatter)
        self.btnReplot.clicked.connect(self.drawReplot)

    def drawScatter(self):
        gb = self.df.groupby('species')
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
        sns.scatterplot(data=self.df, x='sepal_length', y='sepal_width', ax=axes[0], hue='species')
        sns.histplot(data=self.df, x='species', hue='species', ax=axes[1])
        plt.show()

    def drawReplot(self):
        sns.relplot(data=self.df, x='sepal_length', y='sepal_width', kind='scatter', col='species')
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
