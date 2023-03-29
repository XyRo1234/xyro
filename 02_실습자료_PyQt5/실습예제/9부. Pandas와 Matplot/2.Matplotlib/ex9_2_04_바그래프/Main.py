import sys, os

from PyQt5.QtWidgets import *
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

        self.btnBar.clicked.connect(self.drawBar)

    def drawBar(self):
        name = ['Moon', 'Song', 'Lew']
        score = [80, 70, 95]

        plt.figure(1)
        plt.bar(name, score, width=0.5, bottom=20)
        plt.ylabel('score')
        plt.xlabel('name')

        plt.figure(2)
        plt.barh(name, score, left=40, align='edge')
        plt.ylabel('name')
        plt.xlabel('score')

        plt.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
