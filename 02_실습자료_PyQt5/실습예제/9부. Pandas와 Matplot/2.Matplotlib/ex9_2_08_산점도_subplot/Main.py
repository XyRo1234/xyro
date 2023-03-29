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
        """
        Todo 1. 3종에 대한 sepal_length:sepal_width,
        Todo 2. 3종에 대한 petal_length:petal_width의 산점도를 그린다
        :return:
        """
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(6.4 * 2, 4.8))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
