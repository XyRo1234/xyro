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
        self.btnScatter.clicked.connect(self.drawScatter)
        self.btnCmapScatter.clicked.connect(self.drawCmapScatter)

    def drawScatter(self):
        alpha = self.spinAlpha.value()
        plt.scatter(self.df['sepal_length'], self.df['sepal_width'], alpha=alpha)
        plt.scatter(self.df['petal_length'], self.df['petal_width'], alpha=alpha)
        plt.legend(["sepal", 'petal'])
        plt.show()

    def drawCmapScatter(self):
        alpha = self.spinAlpha.value()

        plt.scatter(self.df['sepal_length'], self.df['sepal_width'], c=self.df['sepal_length'],
                    s=self.df['sepal_width'] * 20, alpha=alpha, cmap='plasma')
        plt.scatter(self.df['petal_length'], self.df['petal_width'], c=self.df['sepal_length'],
                    s=self.df['petal_width'] * 30, alpha=alpha, cmap=self.cboColormap.currentText())
        plt.legend(["sepal", 'petal'])
        plt.colorbar()
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
