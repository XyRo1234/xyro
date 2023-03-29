import sys, os

from PyQt5.QtWidgets import *
import seaborn as sns
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
        self.df = pd.read_csv('../tips.csv')
        self.btnDrawRel.clicked.connect(self.drawRelplot)
        self.btnDrawJoint.clicked.connect(self.drawJointplot)

    def drawRelplot(self):
        fg = sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=self.df);
        self.widget.make_plot(fg)

    def drawJointplot(self):
        fg = sns.jointplot(x="total_bill", y="tip", hue="smoker", data=self.df)
        self.widget.make_plot(fg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())

