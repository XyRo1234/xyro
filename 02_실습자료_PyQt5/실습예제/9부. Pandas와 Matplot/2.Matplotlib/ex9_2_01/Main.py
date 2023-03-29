import sys, os

from PyQt5.QtWidgets import *
from matplotlib import pyplot as plt

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnDrawPlot1.clicked.connect(self.drawPlot)
        self.btnDrawPlot2.clicked.connect(self.drawPlot2)
        self.btnDrawPlotXY.clicked.connect(self.DrawPlotXY)
        self.btnDrawPlotList.clicked.connect(self.DrawPlotList)
        self.btnDrawPlotListXY.clicked.connect(self.DrawPlotListXY)
        self.btnScale.clicked.connect(self.Scale)
        self.btnTwoWindow.clicked.connect(self.showMultiWindow)
        self.btnDrawSelect.clicked.connect(self.DrawSelect)

    def drawPlot(self):
        y1 = [5, 6, 3, 2]
        try:
            plt.plot(y1, self.marker.text())
            plt.show()
        except:
            pass

    def drawPlot2(self):
        y1 = [5, 6, 3, 2]
        y2 = [1, 3, 6, 2]
        try:
            plt.plot(y1, self.marker.text())
            plt.plot(y2, self.marker.text())
            plt.show()
        except:
            pass

    def DrawPlotXY(self):
        x = [1, 3, 4, 7]
        y = [5, 6, 3, 2]
        try:
            plt.plot(x, y, self.marker.text())
            plt.show()
        except:
            pass

    def DrawPlotList(self):
        y = [[5, 1], [6, 3], [3, 6], [2, 2]]
        try:
            plt.plot(y, self.marker.text())
            plt.show()
        except:
            pass

    def DrawPlotListXY(self):
        gx = [[1, 5], [3, 7], [5, 9]]
        gy = [[8, 8], [4, 4], [8, 8]]
        try:
            plt.plot(gx, gy, self.marker.text())

            # Todo 다음 데이터로 그래프를 그려보자
            gx1 = [1, 2, 3, 4]
            gy1 = [5, 2, 7, 1]

            gx2 = [3, 4, 5, 6]
            gy2 = [2, 4, 3, 1]

            gx3 = [5, 6, 7, 8]
            gy3 = [1, 9, 5, 3]

            plt.show()
        except:
            pass

    def Scale(self):
        try:
            plt.plot([0.1, 0.2, 0.3, 4], [0.2, 0.3, 2.0, 0.9],
                     self.marker.text(),
                     scalex=self.chkScaleX.isChecked(),
                     scaley=self.chkScaleY.isChecked()
                     )
            plt.show()
        except:
            pass

    def showMultiWindow(self):
        try:
            plt.figure(1)
            y1 = [5, 6, 3, 2]
            plt.plot(y1, self.marker.text())

            plt.figure(2)
            y2 = [1, 3, 6, 2]
            plt.plot(y2, self.marker.text())
            plt.show()
        except:
            pass

    def DrawSelect(self):
        try:
            fig1 = plt.figure(1)
            y1 = [5, 6, 3, 2]
            plt.plot(y1, self.marker.text())

            fig2 = plt.figure(2)
            y2 = [1, 3, 6, 2]
            plt.plot(y2, self.marker.text())
            if self.lineEdit.text() == '1':
                fig1.show()
            elif self.lineEdit.text() == '2':
                fig2.show()
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
