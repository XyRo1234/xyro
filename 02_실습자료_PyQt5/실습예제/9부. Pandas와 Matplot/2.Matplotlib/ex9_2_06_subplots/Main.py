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

        self.btnDraw.clicked.connect(self.drawGraph)
        self.btnSubplot1.clicked.connect(self.drawSubplot1)
        self.btnSubplot2.clicked.connect(self.drawSubplot2)
        self.btnSubplot3.clicked.connect(self.drawSubplot3)

    def drawSubplot1(self):
        name = ['Moon', 'Song', 'Lew']
        score = [80, 70, 95]
        fig = plt.figure()
        axes = fig.subplots(nrows=2, ncols=3)
        axes[0][0].plot(name, score)
        axes[0][2].bar(name, score)
        axes[1][1].scatter(name, score)
        plt.show()

    def drawSubplot2(self):
        name = ['Moon', 'Song', 'Lew']
        score = [80, 70, 95]
        fig, axes = plt.subplots(nrows=2, ncols=3)

        axes[0][0].plot(name, score)
        axes[0][2].bar(name, score)
        axes[1][1].scatter(name,score)

        plt.show()

    def drawSubplot3(self):
        name = ['Moon', 'Song', 'Lew']
        score = [80, 70, 95]
        plt.subplot(231)
        plt.plot(name, score)
        plt.subplot(233)
        plt.bar(name, score)
        plt.subplot(235)
        plt.scatter(name, score)
        plt.show()

    def drawGraph(self):
        name = ['Moon', 'Song', 'Lew']
        score = [80, 70, 95]
        plt.figure(1)
        plt.bar(name, score)
        plt.barh(name, score)

        plt.figure(2)
        y1 = [5, 6, 3, 2]
        y2 = [1, 3, 6, 2]
        plt.plot(y1)
        plt.plot(y2)
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
