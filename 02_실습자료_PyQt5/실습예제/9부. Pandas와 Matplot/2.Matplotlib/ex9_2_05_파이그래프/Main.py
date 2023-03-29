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

        self.btnDrawPie.clicked.connect(self.DrawPie)

    def autopct(self, data):
        res = '{}per'.format(int(data))
        return res

    def DrawPie(self):
        blood = ['A', 'B', 'AB', 'O']
        ratio = [34, 27, 11, 28]
        colors = ['gold', 'red', 'blue', 'green']
        exp = [0, 0, 0, 0.1]

        plt.figure(1)
        plt.pie(ratio, explode=exp, labels=blood, autopct=self.autopct, counterclock=False)

        plt.figure(2)
        plt.pie(ratio, labels=blood, colors=colors, autopct='%.1f%%', shadow=True, pctdistance=0.8)
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
