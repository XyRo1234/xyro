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


    def drawScatter(self):

        
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(6.4*2, 4.8))
        group = self.df.groupby('species')
        species = list(group.groups.keys())

        plt.subplot(121)
        plt.title('sepal scatter')
        plt.xlabel('sepal_length')
        plt.ylabel('sepal_width')
        for group_name, group_df in group:
            plt.scatter(group_df['sepal_length'], group_df['sepal_width'])
        plt.legend(species)

        plt.subplot(122)
        plt.title('petal scatter')
        plt.xlabel('petal_length')
        plt.ylabel('petal_width')
        for group_name, group_df in group:
            plt.scatter(group_df['petal_length'], group_df['petal_width'])
        plt.legend(species)
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
