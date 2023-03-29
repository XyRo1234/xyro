import sys, os

from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow
from pandasModel import *


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
        self.df = pd.DataFrame()
        self.openFile()

        # signal
        self.btnDraw.clicked.connect(self.drawScore)

    def drawScore(self):
        r = self.tableView.currentIndex().row()
        l = self.df.iloc[r, 5:8]
        plt.plot(l, label='score')
        plt.title(self.df.iloc[r, 0])
        plt.xlabel('Subject')
        plt.ylabel('Score')
        plt.legend()
        plt.show()

    def openFile(self):
        file_name = 'score.csv'
        self.df = pd.read_csv(file_name)
        model = pandasModel(self.df)
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
